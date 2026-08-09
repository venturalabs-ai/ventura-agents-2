from __future__ import annotations

import json
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Identidade", "## Domínio", "## Regras de ouro", "## Workflow",
    "## Entradas e saídas", "## Métricas", "## Ferramentas", "## Autonomia", "## Exemplo de uso",
]
REQUIRED_CATEGORIES = {"happy_path", "edge_case", "tool_use", "adversarial", "refusal_safety", "regression"}
FORBIDDEN_CLAIMS = ["certificação mit", "certificado por mit", "certificado pela mit", "100% seguro", "zero vulnerabilidades"]

files = sorted(Path(".").glob("ventura.*.md"))
failures: list[str] = []
if len(files) != 10:
    failures.append(f"expected 10 agent files, found {len(files)}")

agents = {path.stem for path in files}
for path in files:
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"{path}: missing {section}")
    if "humano" not in lowered:
        failures.append(f"{path}: missing human escalation language")
    for claim in FORBIDDEN_CLAIMS:
        if claim in lowered:
            failures.append(f"{path}: unsupported claim language: {claim}")

cases_path = Path("evals/behavioral_cases.jsonl")
seen: set[str] = set()
categories: set[str] = set()
if not cases_path.exists():
    failures.append("missing evals/behavioral_cases.jsonl")
else:
    for line_no, raw in enumerate(cases_path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            case = json.loads(raw)
        except json.JSONDecodeError as exc:
            failures.append(f"behavioral_cases.jsonl:{line_no}: {exc}")
            continue
        case_id = str(case.get("id", "")).strip()
        if not case_id or case_id in seen:
            failures.append(f"behavioral_cases.jsonl:{line_no}: missing/duplicate id")
        seen.add(case_id)
        categories.add(str(case.get("category", "")).strip())
        if str(case.get("expected_agent", "")).strip() not in agents:
            failures.append(f"behavioral_cases.jsonl:{line_no}: invalid expected_agent")
        if not case.get("required_all") and not case.get("required_any"):
            failures.append(f"behavioral_cases.jsonl:{line_no}: no positive criteria")
        if not case.get("forbidden"):
            failures.append(f"behavioral_cases.jsonl:{line_no}: no forbidden criteria")

missing = sorted(REQUIRED_CATEGORIES - categories)
if missing:
    failures.append("missing eval categories: " + ", ".join(missing))
if not Path("scripts/score_behavioral_outputs.py").exists():
    failures.append("missing scripts/score_behavioral_outputs.py")

if failures:
    print("AGENT-2 EVALS: FAIL")
    for failure in failures:
        print(f"- {failure}")
    raise SystemExit(1)
print(f"AGENT-2 EVALS: PASS ({len(files)} agents; {len(seen)} behavioral cases)")
print("Model-quality claims require externally generated, versioned outputs and provider metadata.")
