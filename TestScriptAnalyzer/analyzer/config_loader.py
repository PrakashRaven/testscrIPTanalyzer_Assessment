import yaml
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class Config:
    rules: List[Dict[str, Any]]
    duplication: Dict[str, Any]

def load_config(path: str) -> Config:
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    return Config(rules=cfg.get("rules", []), duplication=cfg.get("duplication", {}))
