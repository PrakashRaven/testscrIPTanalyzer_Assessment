import argparse, os
from .config_loader import load_config
from .scanner import RuleScanner
from .duplication import DuplicateDetector
from .utils import list_test_files
from .reporting import write_issues_csv, generate_summary_table

def run_analyzer(input_dir: str, config_path: str, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    cfg = load_config(config_path)
    scanner = RuleScanner(cfg.rules)
    all_issues = []
    test_files = []
    for path, lang in list_test_files(input_dir):
        test_files.append(path)
        all_issues.extend(scanner.scan_file(path, lang))
    dup_cfg = cfg.duplication or {}
    detector = DuplicateDetector(min_block_lines=dup_cfg.get("min_block_lines",4), ignore_patterns=dup_cfg.get("ignore_patterns",[]))
    duplicates = detector.analyze(test_files)
    issues_csv = os.path.join(out_dir, "issues_report.csv")
    write_issues_csv(all_issues, issues_csv)
    summary_md = os.path.join(out_dir, "summary_table.md")
    summary = generate_summary_table(all_issues)
    with open(summary_md, "w", encoding="utf-8") as f:
        f.write("# Code Review Analytics Summary\n\n")
        f.write("## Issues by File and Severity\n\n")
        f.write(summary)
        f.write("\n\n## Duplicate Blocks\n\n")
        if not duplicates:
            f.write("_No duplicates found above threshold._\n")
        else:
            for b in duplicates:
                f.write(f"- Duplicate block `{b.hash[:8]}` appears in:\n")
                for p,l in b.locations:
                    f.write(f"  - `{p}` at ~line {l}\n")
                f.write("```text\n")
                f.write("\n".join(b.lines[:10]))
                f.write("\n```\n\n")
    print(f"Issues written to: {issues_csv}")
    print(f"Summary written to: {summary_md}")

def main():
    parser = argparse.ArgumentParser(description="Analyzer for Playwright tests")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--config", default="config/rules.yml")
    parser.add_argument("--out-dir", default="reports")
    args = parser.parse_args()
    run_analyzer(args.input_dir, args.config, args.out_dir)

if __name__ == '__main__':
    main()
