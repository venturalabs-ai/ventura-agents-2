#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, default=Path("evals/behavioral_cases.jsonl"))
    parser.add_argument("--outputs", type=Path, required=True)
    args = parser.parse_args()
    cases = {row["id"]: row for row in load(args.cases)}
    outputs = {row["id"]: row for row in load(args.outputs)}
    missing = sorted(set(cases) - set(outputs))
    if missing:
        print("missing outputs: " + ", ".join(missing))
        return 2
    failed: set[str] = set()
    categories: dict[str, list[bool]] = {}
    for case_id, case in cases.items():
        result = outputs[case_id]
        text = str(result.get("output", "")).lower()
        reasons = []
        if str(result.get("selected_agent", "")).strip().lower() != str(case["expected_agent"]).lower():
            reasons.append("wrong agent")
        required_all = [str(x).lower() for x in case.get("required_all", [])]
        required_any = [str(x).lower() for x in case.get("required_any", [])]
        forbidden = [str(x).lower() for x in case.get("forbidden", [])]
        missing_all = [x for x in required_all if x not in text]
        if missing_all:
            reasons.append("missing: " + ", ".join(missing_all))
        if required_any and not any(x in text for x in required_any):
            reasons.append("missing any-of: " + ", ".join(required_any))
        present = [x for x in forbidden if x in text]
        if present:
            reasons.append("forbidden: " + ", ".join(present))
        ok = not reasons
        categories.setdefault(case["category"], []).append(ok)
        if not ok:
            failed.add(case_id)
        print(f"{case_id}: {'PASS' if ok else 'FAIL'}" + (" — " + "; ".join(reasons) if reasons else ""))
    score = (len(cases) - len(failed)) / max(len(cases), 1)
    print(f"task_success={score:.3f}")
    for category, values in sorted(categories.items()):
        print(f"category.{category}={sum(values)/len(values):.3f}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
