import os
from typing import Generator, Tuple, List

SUPPORTED_EXT = {".py": "py", ".js": "js", ".ts": "ts", ".java": "java"}

def list_test_files(root_dir: str) -> Generator[Tuple[str, str], None, None]:
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            ext = os.path.splitext(fname)[1]
            if ext in SUPPORTED_EXT:
                yield os.path.join(dirpath, fname), SUPPORTED_EXT[ext]

def read_file_lines(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.readlines()
