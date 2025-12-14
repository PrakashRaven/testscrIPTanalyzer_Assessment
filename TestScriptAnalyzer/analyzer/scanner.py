import re
from dataclasses import dataclass
from typing import List, Dict, Any
from .utils import read_file_lines

@dataclass
class Issue:
    rule_id: str
    file_path: str
    line_no: int
    severity: str
    description: str
    snippet: str
    tags: List[str]

class RuleScanner:
    def __init__(self, rules: List[Dict[str, Any]]):
        self.compiled_rules = []
        for r in rules:
            if "id" not in r or "pattern" not in r or "languages" not in r:
                continue
            try:
                regex = re.compile(r["pattern"])
            except re.error:
                continue
            self.compiled_rules.append({
                "id": r["id"],
                "description": r.get("description",""),
                "severity": r.get("severity","LOW"),
                "tags": r.get("tags",[]),
                "languages": set(r.get("languages",[])),
                "regex": regex,
            })

    def scan_file(self, file_path: str, lang: str) -> List[Issue]:
        issues: List[Issue] = []
        lines = read_file_lines(file_path)
        for rule in self.compiled_rules:
            if lang not in rule["languages"]:
                continue
            for idx, line in enumerate(lines, start=1):
                if rule["regex"].search(line):
                    issues.append(Issue(rule_id=rule["id"], file_path=file_path, line_no=idx,
                                        severity=rule["severity"], description=rule["description"],
                                        snippet=line.strip()[:200], tags=list(rule["tags"])))
        return issues
