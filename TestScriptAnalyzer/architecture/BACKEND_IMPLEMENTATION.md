
# Backend Implementation (Detailed)

## Overview
The analyzer acts as the backend engine of the project. It processes test script files, applies rule-based logic, performs duplication detection, and generates structured reports.

## Components
### 1. Config Loader
- Reads rules.yml
- Builds rule list and duplication settings

### 2. Rule Scanner
- Reads file line-by-line
- Applies compiled regex rules
- Emits Issue objects

### 3. Duplication Detector
- Normalizes lines
- Builds fixed-size rolling code blocks
- Hashes blocks
- Reports repeated sequences

### 4. Reporting Engine
- Writes CSV of issues
- Writes Markdown summary
- Produces chart and Excel report

## Backend Flow
Input → Load Config → Scan Files → Detect Duplicates → Generate Reports → Output Artifacts
