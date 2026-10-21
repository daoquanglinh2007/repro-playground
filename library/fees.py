"""Late fees for borrowed items.

Library policy (printed on the poster at the front desk):
  * the first GRACE_DAYS days after the due date are free;
  * after that, every late day is charged at DAILY_FEE_PENCE;
  * no single loan is ever charged more than FEE_CAP_PENCE.
"""
from __future__ import annotations

from datetime import date

GRACE_DAYS = 2
DAILY_FEE_PENCE = 20
FEE_CAP_PENCE = 500


def days_late(due: date, returned: date) -> int:
    """Whole days between the due date and the return date (never negative)."""
    return max(0, (returned - due).days)


def late_fee(due: date, returned: date) -> int:
    """The fee, in pence, for an item returned on `returned`."""
    late = days_late(due, returned)
    if late < GRACE_DAYS:
        return 0
    return min(late * DAILY_FEE_PENCE, FEE_CAP_PENCE)
