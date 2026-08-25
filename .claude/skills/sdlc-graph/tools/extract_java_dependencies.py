#!/usr/bin/env python3
"""Extract database tables and Kafka topics from runtime client declarations.

Database tables intentionally come from application client code (Spring Data,
JPA mappings, native repository queries, and JdbcTemplate calls). Migration SQL
is never read because it describes ownership/history, not necessarily runtime use.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

TABLE_ANNOTATION = re.compile(r"@Table\s*\(\s*(?:name\s*=\s*)?[\"']([^\"']+)[\"']", re.S)
CLASS = re.compile(r"\bclass\s+(\w+)")
REPOSITORY = re.compile(r"\binterface\s+(\w+)\s+extends\s+[\w.]*Repository\s*<\s*(\w+)\s*,", re.S)
BASE_MAPPER = re.compile(r"\binterface\s+(\w+)\s+extends\s+[\w.]*BaseMapper\s*<\s*(\w+)\s*>", re.S)
SQL_TABLE = re.compile(r"\b(?:from|join|update|into|delete\s+from)\s+([A-Za-z_][\w.$]*)", re.I)
WRITE_SQL = re.compile(r"\b(?:insert\s+into|update|delete\s+from)\b", re.I)
NATIVE_QUERY = re.compile(r"@Query\s*\(\s*(?:value\s*=\s*)?[\"']([^\"']+)[\"'](?:(?!\)).)*nativeQuery\s*=\s*true(?:(?!\)).)*\)", re.I | re.S)
JDBC_CALL = re.compile(r"\b(?:jdbcTemplate|namedParameterJdbcTemplate)\.\w+\s*\(\s*[\"']([^\"']+)[\"']", re.I | re.S)
CONFIG_TOPIC = re.compile(r"(?im)^[ \t]*([\w.-]*(?:topic|route)[\w.-]*)[ \t]*:[ \t]*(?:kafka://|kafka:)?([^\s?#]+)")
JAVA_TOPIC_LITERAL = re.compile(r"\b([A-Za-z_]\w*(?:TOPIC|Topic)\w*)\s*=\s*[\"']([^\"']+)[\"']")
TOPIC_SECTION = re.compile(r"(?m)^([ \t]*)topic:[ \t]*$\n((?:(?:\1[ \t]+)[^\n]*\n?)*)")


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def topic_direction(key: str, topic: str) -> str:
    clue = f"{key} {topic}".lower()
    if any(word in clue for word in ("input", "inbound", "consumer", "_in", "-in", "record_in")):
        return "CONSUMES"
    if any(word in clue for word in ("output", "outbound", "publish", "producer", "send", "enriched", "_out", "-out")):
        return "PUBLISHES"
    return "CONFIGURED"


def extract(repo: Path) -> dict[str, list[dict[str, Any]]]:
    java_root = repo / "src" / "main" / "java"
    resource_root = repo / "src" / "main" / "resources"
    entities: dict[str, tuple[str, str, int]] = {}
    classes: dict[str, tuple[str, int]] = {}
    files: list[tuple[Path, str]] = []
    if java_root.exists():
        for path in sorted(java_root.rglob("*.java")):
            text = read_text(path)
            if text is None:
                continue
            files.append((path, text))
            table = TABLE_ANNOTATION.search(text)
            klass = CLASS.search(text)
            if klass:
                classes[klass.group(1)] = (
                    path.relative_to(repo).as_posix(), line_number(text, klass.start())
                )
            if table and klass:
                entities[klass.group(1)] = (
                    table.group(1).lower(), path.relative_to(repo).as_posix(), line_number(text, table.start())
                )

    tables: dict[tuple[str, str, str], dict[str, Any]] = {}
    for path, text in files:
        relative = path.relative_to(repo).as_posix()
        repository = REPOSITORY.search(text)
        if repository and repository.group(2) in entities:
            table, entity_path, entity_line = entities[repository.group(2)]
            key = (table, relative, "READ_WRITE")
            tables[key] = {
                "name": table, "access": "READ_WRITE", "client": "SPRING_DATA",
                "path": relative, "line": line_number(text, repository.start()),
                "related_paths": [relative, entity_path], "entity_line": entity_line,
            }
        mapper = BASE_MAPPER.search(text)
        if mapper and mapper.group(2) in classes:
            entity = mapper.group(2)
            entity_path, entity_line = classes[entity]
            table = entities.get(entity, (camel_to_snake(entity), entity_path, entity_line))[0]
            key = (table, relative, "READ_WRITE")
            tables.setdefault(key, {
                "name": table, "access": "READ_WRITE", "client": "MYBATIS_PLUS_CONVENTION",
                "path": relative, "line": line_number(text, mapper.start()),
                "related_paths": [relative, entity_path], "entity_line": entity_line,
                "assertion_status": "INFERRED", "score": 0.75,
            })
        client_queries = [(match, "NATIVE_QUERY") for match in NATIVE_QUERY.finditer(text)]
        client_queries.extend((match, "JDBC_TEMPLATE") for match in JDBC_CALL.finditer(text))
        for declaration, client in client_queries:
            sql = declaration.group(1)
            for match in SQL_TABLE.finditer(sql):
                table = match.group(1).split(".")[-1].lower()
                access = "WRITE" if WRITE_SQL.search(sql) else "READ"
                key = (table, relative, access)
                tables[key] = {
                    "name": table, "access": access, "client": client,
                    "path": relative, "line": line_number(text, declaration.start()),
                    "related_paths": [relative],
                }

    mapper_root = resource_root / "mapperxml"
    if mapper_root.exists():
        for path in sorted(mapper_root.rglob("*.xml")):
            text = read_text(path)
            if text is None:
                continue
            relative = path.relative_to(repo).as_posix()
            sql_text = re.sub(r"<!--.*?-->|<[^>]+>", lambda item: "\n" * item.group(0).count("\n"), text, flags=re.S)
            for match in SQL_TABLE.finditer(sql_text):
                table = match.group(1).split(".")[-1].lower()
                operation = match.group(0).lstrip().split(None, 1)[0].upper()
                access = "READ" if operation in {"FROM", "JOIN"} else "WRITE"
                key = (table, relative, access)
                tables[key] = {
                    "name": table, "access": access, "client": "MYBATIS_MAPPER",
                    "path": relative, "line": line_number(sql_text, match.start()),
                    "related_paths": [relative],
                }

    topics: dict[tuple[str, str], dict[str, Any]] = {}
    for root in (java_root, resource_root):
        if not root.exists():
            continue
        for path in sorted(item for item in root.rglob("*") if item.suffix in {".java", ".yml", ".yaml", ".properties"}):
            text = read_text(path)
            if text is None or "kafka" not in text.lower():
                continue
            relative = path.relative_to(repo).as_posix()
            declarations: list[tuple[str, str, int]] = []
            for match in CONFIG_TOPIC.finditer(text):
                key, topic = match.group(1), match.group(2).strip("\"'")
                declarations.append((topic, topic_direction(key, topic), match.start()))
            for section in TOPIC_SECTION.finditer(text):
                for child in re.finditer(r"(?m)^[ \t]+([\w.-]+)[ \t]*:[ \t]*([^\s#]+)", section.group(2)):
                    key, topic = child.group(1), child.group(2).strip("\"'")
                    declarations.append((topic, topic_direction(key, topic), section.start(2) + child.start()))
            for match in JAVA_TOPIC_LITERAL.finditer(text):
                declarations.append((match.group(2), topic_direction(match.group(1), match.group(2)), match.start()))
            for topic, direction, offset in declarations:
                topic = re.sub(r"^kafka:(?://)?", "", topic)
                if topic.lower() in {"kafka", "enabled", "true", "false"} or topic.startswith(("file:", "/", "-")):
                    continue
                if topic.isupper() and topic.endswith("_TOPIC"):
                    continue
                topics[(topic, relative)] = {
                    "name": topic, "direction": direction, "path": relative, "line": line_number(text, offset)
                }
    return {"tables": sorted(tables.values(), key=lambda item: (item["name"], item["path"])),
            "topics": sorted(topics.values(), key=lambda item: (item["name"], item["path"]))}


def camel_to_snake(value: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path)
    args = parser.parse_args()
    print(json.dumps(extract(args.repository.resolve()), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
