#!/usr/bin/env python3
"""Render graph.json as a self-contained dependency graph viewer."""

from __future__ import annotations

import argparse
import json
import platform
import subprocess
from pathlib import Path


TEMPLATE = r'''<div id="sdlc-graph-view">
<style>
#sdlc-graph-view{--fg:light-dark(#17211f,#eef6f2);--muted:light-dark(#60706a,#9aaca5);--border:light-dark(#ccd8d2,#33443e);--surface:light-dark(#f7faf8,#111917);color:var(--fg);font:13px/1.35 ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;max-width:1200px;margin:auto}#sdlc-graph-view *{box-sizing:border-box}.head{display:flex;justify-content:space-between;gap:16px;align-items:end;border-bottom:1px solid var(--border);padding:4px 0 12px}.head h1{font-size:20px;margin:0;font-weight:650}.sub,.metrics,.detail-type{color:var(--muted)}.metrics{text-align:right;white-space:nowrap}.body{display:grid;grid-template-columns:minmax(0,1fr) 255px;gap:14px;padding-top:12px}.plot{min-width:0;border:1px solid var(--border);background:var(--surface)}svg{display:block;width:100%;height:680px}.side{border-left:1px solid var(--border);padding-left:14px;overflow-wrap:anywhere}.side h2{font-size:13px;margin:3px 0 8px}.detail-name{font-size:15px;font-weight:650}.meta{display:grid;grid-template-columns:68px 1fr;gap:6px;margin:12px 0}.meta dt{color:var(--muted)}.meta dd{margin:0}.links{display:grid;gap:7px;max-height:330px;overflow:auto}.links div{color:var(--muted)}.links b{color:var(--fg);font-weight:600}.legend{display:flex;flex-wrap:wrap;gap:8px 13px;padding:10px}.legend button{border:0;background:transparent;color:var(--fg);padding:0;cursor:pointer;font:inherit}.legend button[aria-pressed=false]{color:var(--muted)}.swatch{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px}.node{stroke:var(--surface);stroke-width:1.4px;cursor:pointer}.node.selected{stroke:var(--fg);stroke-width:3px}.label{fill:var(--fg);font-size:10px;pointer-events:none}.link{stroke-width:1.15px;opacity:.5}.link.off{opacity:.07}.tip{position:fixed;display:none;pointer-events:none;background:light-dark(#fff,#1b2723);border:1px solid var(--border);padding:7px 9px;max-width:260px;z-index:4}@media(max-width:760px){.head{align-items:start;flex-direction:column}.metrics{text-align:left}.body{grid-template-columns:1fr}.side{border-left:0;border-top:1px solid var(--border);padding:12px 0 0}svg{height:570px}}
</style>
<style>.node-controls{display:flex;flex-wrap:wrap;gap:8px 13px;padding:10px 10px 0}.node-controls button{border:0;background:transparent;color:var(--fg);padding:0;cursor:pointer;font:inherit}.node-controls button[aria-pressed=false]{color:var(--muted)}.features{display:grid;gap:6px;max-height:300px;overflow:auto}.features div{color:var(--muted)}</style>
<div class="head"><div><h1>Dependency graph</h1><div class="sub">Services, data stores, messaging, libraries, and external dependencies</div></div><div class="metrics"><strong>__TOTAL_NODES__</strong> nodes · <strong>__TOTAL_EDGES__</strong> edges</div></div>
<div class="body"><div class="plot"><div class="node-controls" aria-label="Node layers"></div><svg role="img" aria-label="Interactive dependency graph"></svg><div class="legend"></div></div><aside class="side" aria-live="polite"><h2>Selected node</h2><div class="detail-name">Choose a node</div><div class="detail-type">Relationships appear here</div><dl class="meta"></dl><h2>Connections</h2><div class="links"></div><h2>Business features</h2><div class="features"></div></aside></div><div class="tip" role="tooltip"></div>
<script>window.__SDLC_GRAPH__=__GRAPH_DATA__;</script><script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script><script>
(()=>{const root=document.getElementById("sdlc-graph-view"),data=__GRAPH_DATA__,svg=d3.select(root.querySelector("svg")),plot=root.querySelector(".plot"),tip=root.querySelector(".tip"),colors={Service:"#0f766e",Feature:"#d97706",Database:"#2563eb",Schema:"#4f46e5",Table:"#818cf8",MessageBroker:"#d97706",MessageQueue:"#be123c",ExternalDependency:"#b91c1c",Library:"#15803d",API:"#7c3aed",Endpoint:"#a78bfa"},edgeColors={CALLS:"#0f766e",CONNECTS_TO:"#2563eb",DEPENDS_ON:"#15803d",IMPLEMENTS:"#d97706",CONTAINS:"#4f46e5",PROVIDES:"#7c3aed",PUBLISHES:"#be123c",SUBSCRIBES_TO:"#d97706",READS_FROM:"#2563eb",WRITES_TO:"#b91c1c"},types=[...new Set(data.edges.map(d=>d.type))].sort(),enabled=new Set(types),legend=d3.select(root.querySelector(".legend"));types.forEach(t=>{const b=legend.append("button").attr("type","button").attr("aria-pressed",true).on("click",()=>{enabled.has(t)?enabled.delete(t):enabled.add(t);b.attr("aria-pressed",enabled.has(t));links.classed("off",d=>!enabled.has(d.type))});b.append("span").attr("class","swatch").style("background",edgeColors[t]||"#60706a");b.append("span").text(t)});const defs=svg.append("defs");defs.append("marker").attr("id","arrow").attr("viewBox","0 -4 8 8").attr("refX",14).attr("refY",0).attr("markerWidth",5).attr("markerHeight",5).attr("orient","auto").append("path").attr("d","M0,-4L8,0L0,4Z").style("fill","#60706a");const stage=svg.append("g"),linkLayer=stage.append("g"),nodeLayer=stage.append("g"),labelLayer=stage.append("g"),links=linkLayer.selectAll("line").data(data.edges).join("line").attr("class","link").attr("stroke",d=>edgeColors[d.type]||"#60706a").attr("marker-end","url(#arrow)"),nodes=nodeLayer.selectAll("circle").data(data.nodes).join("circle").attr("class","node").attr("r",d=>d.type==="Service"?9:d.type==="Feature"?7:d.type==="Database"||d.type==="MessageBroker"?8:5).attr("fill",d=>colors[d.type]||"#60706a").on("mouseenter",(e,d)=>{tip.style.display="block";tip.textContent=d.type+": "+d.name;tip.style.left=e.clientX+12+"px";tip.style.top=e.clientY+12+"px"}).on("mousemove",e=>{tip.style.left=e.clientX+12+"px";tip.style.top=e.clientY+12+"px"}).on("mouseleave",()=>tip.style.display="none").on("click",(e,d)=>select(d)),labels=labelLayer.selectAll("text").data(data.nodes.filter(d=>["Service","Feature","Database","MessageBroker","MessageQueue","ExternalDependency"].includes(d.type))).join("text").attr("class","label").text(d=>d.name),sim=d3.forceSimulation(data.nodes).force("link",d3.forceLink(data.edges).id(d=>d.id).distance(d=>d.type==="CALLS"?90:55).strength(.55)).force("charge",d3.forceManyBody().strength(-145)).force("center",d3.forceCenter()).force("collision",d3.forceCollide().radius(14));function select(d){nodes.classed("selected",n=>n.id===d.id);root.querySelector(".detail-name").textContent=d.name;root.querySelector(".detail-type").textContent=d.type;const meta=root.querySelector(".meta");meta.replaceChildren();[["id",d.id],["links",String(data.edges.filter(e=>e.source.id===d.id||e.target.id===d.id).length)]].forEach(([k,v])=>{const a=document.createElement("dt"),b=document.createElement("dd");a.textContent=k;b.textContent=v;meta.append(a,b)});const list=root.querySelector(".links");list.replaceChildren();data.edges.filter(e=>e.source.id===d.id||e.target.id===d.id).slice(0,18).forEach(e=>{const row=document.createElement("div"),other=e.source.id===d.id?e.target:e.source;row.textContent=e.type+" "+(e.source.id===d.id?"→":"←")+" "+other.name;list.append(row)})}function resize(){const w=plot.getBoundingClientRect().width;svg.attr("viewBox",`0 0 ${Math.max(320,w)} 680`);sim.force("center",d3.forceCenter(Math.max(160,w/2),340)).alpha(.2).restart()}sim.on("tick",()=>{links.attr("x1",d=>d.source.x).attr("y1",d=>d.source.y).attr("x2",d=>d.target.x).attr("y2",d=>d.target.y);nodes.attr("cx",d=>d.x).attr("cy",d=>d.y);labels.attr("x",d=>d.x+9).attr("y",d=>d.y+3)});nodes.call(d3.drag().on("start",(e,d)=>{if(!e.active)sim.alphaTarget(.2).restart();d.fx=d.x;d.fy=d.y}).on("drag",(e,d)=>{d.fx=e.x;d.fy=e.y}).on("end",(e,d)=>{if(!e.active)sim.alphaTarget(0);d.fx=null;d.fy=null}));svg.call(d3.zoom().scaleExtent([.4,3]).on("zoom",e=>stage.attr("transform",e.transform)));new ResizeObserver(resize).observe(plot);resize();select(data.nodes.find(d=>d.type==="Service")||data.nodes[0])})();
</script><script>
(()=>{const data=window.__SDLC_GRAPH__,root=document.getElementById("sdlc-graph-view"),allowed=new Set(["Service","Database","MessageBroker","MessageQueue","ExternalDependency"]),types=[...new Set(data.nodes.map(n=>n.type))].sort(),controls=root.querySelector(".node-controls"),features=root.querySelector(".features");types.forEach(type=>{const b=document.createElement("button");b.type="button";b.setAttribute("aria-pressed",allowed.has(type));b.textContent=(allowed.has(type)?"Shown: ":"Hidden: ")+type;b.onclick=()=>{allowed.has(type)?allowed.delete(type):allowed.add(type);b.setAttribute("aria-pressed",allowed.has(type));b.textContent=(allowed.has(type)?"Shown: ":"Hidden: ")+type;apply()};controls.append(b)});function apply(){const svg=root.querySelector("svg"),visible=new Set(data.nodes.filter(n=>allowed.has(n.type)).map(n=>n.id));svg.querySelectorAll("circle").forEach(el=>{const d=el.__data__;el.style.display=visible.has(d.id)?"":"none"});svg.querySelectorAll("text").forEach(el=>{const d=el.__data__;el.style.display=d&&visible.has(d.id)?"":"none"});svg.querySelectorAll("line").forEach(el=>{const d=el.__data__,source=d&&d.source&&d.source.id,target=d&&d.target&&d.target.id;el.style.display=source&&target&&visible.has(source)&&visible.has(target)?"":"none"})}function renderFeatures(serviceId){features.replaceChildren();const repo=(serviceId||"").split("/").pop(),rows=data.features?.[repo]||[];rows.forEach(f=>{const row=document.createElement("div");row.textContent="• "+f.name;features.append(row)});if(!rows.length){const row=document.createElement("div");row.textContent="Select a service to see its feature catalog.";features.append(row)}}root.querySelectorAll("circle").forEach(el=>el.addEventListener("click",()=>{const d=el.__data__;if(d?.type==="Service")renderFeatures(d.id)}));renderFeatures("service:ratan-release-impact/orchestration");apply()})();
</script></div>'''


def open_view(path: Path) -> None:
    system = platform.system()
    command = ["open", str(path)] if system == "Darwin" else ["xdg-open", str(path)]
    try:
        subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Render graph.json as an interactive HTML dependency view")
    parser.add_argument("--graph", type=Path, default=Path("graph/graph.json"))
    parser.add_argument("--out", type=Path, default=Path("graph/sdlc-graph.html"))
    parser.add_argument("--no-open", action="store_true")
    args = parser.parse_args()
    graph = json.loads(args.graph.read_text(encoding="utf-8"))
    nodes = [{"id": n["id"], "type": n["type"], "name": n["name"]} for n in graph["nodes"]]
    ids = {n["id"] for n in nodes}
    edges = [{"source": e["source"], "target": e["target"], "type": e["type"]} for e in graph["edges"] if e["source"] in ids and e["target"] in ids]
    data = json.dumps({"nodes": nodes, "edges": edges, "features": graph.get("features", {})}, separators=(",", ":"))
    html = TEMPLATE.replace("__TOTAL_NODES__", str(len(nodes))).replace("__TOTAL_EDGES__", str(len(edges))).replace("__GRAPH_DATA__", data)
    html = html.replace('allowed=new Set(["Service","Database","MessageBroker","MessageQueue","ExternalDependency"])',
                        'allowed=new Set(["Service","Feature","Database","MessageBroker","MessageQueue","ExternalDependency"])')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(html, encoding="utf-8")
    print(args.out.resolve())
    if not args.no_open:
        open_view(args.out.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
