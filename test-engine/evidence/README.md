# Test Evidence

`run_evidence.sh` writes immutable before/after evidence below a change ID.
Portable `run.json`, `comparison.json`, and `impact-fragment.md` artifacts may be
reviewed and versioned. Bulky Robot HTML/XML under `raw/` is ignored.

No artifact is production evidence. Every run is classified as
`observed_in_test_engine_simulation` and records the mocked boundaries.
