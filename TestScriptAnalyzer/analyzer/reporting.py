import csv
from collections import Counter, defaultdict
from typing import List
from .scanner import Issue

def write_issues_csv(issues: List[Issue], out_path: str):
    with open(out_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["rule_id","severity","file_path","line_no","description","snippet","tags"])
        for i in issues:
            writer.writerow([i.rule_id,i.severity,i.file_path,i.line_no,i.description,i.snippet,",".join(i.tags)])

def generate_summary_table(issues: List[Issue]) -> str:
    file_severity = defaultdict(Counter)
    for i in issues:
        file_severity[i.file_path][i.severity] += 1
    lines = ["| File | HIGH | MEDIUM | LOW | Total |", "|------|------|--------|-----|-------|"]
    for fpath,sev in sorted(file_severity.items()):
        high = sev.get("HIGH",0); med=sev.get("MEDIUM",0); low=sev.get("LOW",0)
        total = high+med+low
        lines.append(f"| `{fpath}` | {high} | {med} | {low} | {total} |")
    if len(lines)<=2:
        lines.append("| _no issues_ | 0 | 0 | 0 | 0 |")
    return "\n".join(lines)
