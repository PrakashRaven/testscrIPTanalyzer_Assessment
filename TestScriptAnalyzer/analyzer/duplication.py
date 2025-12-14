import hashlib, re
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Tuple
from .utils import read_file_lines

@dataclass
class DuplicateBlock:
    hash: str
    locations: List[Tuple[str,int]]
    lines: List[str]

class DuplicateDetector:
    def __init__(self, min_block_lines: int = 4, ignore_patterns=None):
        self.min_block_lines = max(2, min_block_lines)
        self.ignore_patterns = [re.compile(p) for p in (ignore_patterns or [])]

    def _normalize_line(self, line: str) -> str:
        return line.strip()

    def _should_ignore(self, line: str) -> bool:
        return any(p.match(line) for p in self.ignore_patterns)

    def analyze(self, files: List[str]) -> List[DuplicateBlock]:
        index = defaultdict(list)
        blocks = {}
        for path in files:
            raw = read_file_lines(path)
            filtered = [l for l in raw if not self._should_ignore(l)]
            norm = [self._normalize_line(l) for l in filtered]
            for i in range(0, len(norm) - self.min_block_lines + 1):
                block = norm[i:i+self.min_block_lines]
                block_str = "\n".join(block)
                h = hashlib.sha1(block_str.encode("utf-8")).hexdigest()
                index[h].append((path, i+1))
                if h not in blocks:
                    blocks[h] = DuplicateBlock(hash=h, locations=[], lines=block)
        duplicates = []
        for h, locs in index.items():
            if len(locs) >= 2:
                b = blocks[h]
                b.locations = locs
                duplicates.append(b)
        return duplicates
