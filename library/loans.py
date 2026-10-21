"""How long each kind of item may be borrowed for."""
from __future__ import annotations

from datetime import date, timedelta

#: Loan periods in days. DVDs are short loans on purpose: there are few copies.
LOAN_DAYS = {"book": 21, "audiobook": 14, "dvd": 3}


def due_date(kind: str, borrowed: date) -> date:
    """The date an item of `kind` borrowed on `borrowed` must come back."""
    try:
        days = LOAN_DAYS[kind]
    except KeyError:
        raise ValueError(f"unknown item kind: {kind!r}") from None
    return borrowed + timedelta(days=days)
