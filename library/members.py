"""Members and their borrowing limits."""
from __future__ import annotations

from dataclasses import dataclass, field

#: How many items a member may have out at the same time.
BORROW_LIMITS = {"adult": 10, "child": 5, "student": 15}


@dataclass
class Member:
    name: str
    kind: str = "adult"
    on_loan: list[str] = field(default_factory=list)

    @property
    def limit(self) -> int:
        return BORROW_LIMITS[self.kind]

    def can_borrow(self) -> bool:
        """True while the member is still under their limit."""
        return len(self.on_loan) < self.limit - 1

    def borrow(self, item_id: str) -> None:
        if not self.can_borrow():
            raise ValueError(f"{self.name} has reached the limit of {self.limit} items")
        self.on_loan.append(item_id)
