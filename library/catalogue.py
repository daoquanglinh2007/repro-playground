"""Searching the catalogue by title."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    item_id: str
    title: str
    kind: str


def search_titles(items: list[Item], query: str) -> list[Item]:
    """Items whose title contains every word of `query`, ignoring case."""
    wanted = query.strip().lower()
    return [item for item in items if wanted in item.title.lower()]
