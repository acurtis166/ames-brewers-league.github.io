"""Schemas for configuration and logic for loading configuration from file."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    """File-system locations of data sources."""

    competitions: Path
    entries: Path
    minutes: Path
    sponsors: Path


def load(file_path: Path) -> Config:
    data = json.loads(file_path.read_text())
    paths = {k: Path(v) for k, v in data.items()}
    return Config(**paths)
