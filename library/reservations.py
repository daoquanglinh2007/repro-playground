"""Holds (reservations) on items that are currently out on loan."""
from __future__ import annotations


class HoldQueue:
    """Members waiting for one title, in the order they placed their hold."""

    def __init__(self) -> None:
        self._waiting: list[str] = []

    def place_hold(self, member: str) -> int:
        """Add a member to the queue and return their position (1 = next)."""
        if member in self._waiting:
            return self.position_of(member)
        self._waiting.append(member)
        return len(self._waiting)

    def position_of(self, member: str) -> int:
        """1-based position of `member` in the queue."""
        return self._waiting.index(member) + 1

    def next_borrower(self) -> str | None:
        """Who gets the item when it comes back. Removes them from the queue."""
        if not self._waiting:
            return None
        return self._waiting.pop()

    def __len__(self) -> int:
        return len(self._waiting)
