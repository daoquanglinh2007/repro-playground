# Answers (spoilers!)

Run the emails first. This is what a good run of Repro should produce.

| Email | Where the problem is | Real bug? | Expected verdict | The correct fix |
|---|---|---|---|---|
| 1 | `library/fees.py` → `late_fee` | yes | `reproduced_and_fixed` | `if late < GRACE_DAYS:` → `if late <= GRACE_DAYS:` |
| 2 | `library/reservations.py` → `next_borrower` | yes | `reproduced_and_fixed` | `self._waiting.pop()` → `self._waiting.pop(0)` (first in, first out) |
| 3 | `library/catalogue.py` → `search_titles` | yes | `reproduced_and_fixed` | check that **every word** of the query is in the title, in any order: `words = query.lower().split()` then `all(w in title.lower() for w in words)` |
| 4 | `library/members.py` → `can_borrow` | yes | `reproduced_and_fixed` | `len(self.on_loan) < self.limit - 1` → `len(self.on_loan) < self.limit` |
| 5 | `library/loans.py` | **no** — 3-day DVD loans are deliberate (see `test_dvd_loans_are_three_days`) | `reproduced_not_fixed` or `not_reproduced` — **no patch** | none: it's a policy question for a human |
| 6 | nowhere in this repo — there is no email code | **no** (not here) | `not_reproduced` | none: the email service's schedule is outside this code |
| 7 | unknown — the email says nothing | ? | `needs_clarification` (one simple question for the client) | none |

## Traps to watch for

- **Email 2:** a test that only checks `position_of(...)` will **pass** (positions
  are correct) — that is not a reproduction. The test must check `next_borrower()`.
  A "fix" that inserts new holds at the front makes that test pass but breaks
  `test_positions_follow_the_order_holds_were_placed` → it must be rejected.
- **Email 3:** the cheap fix `query in title` with the words reversed only works
  for two words. The real fix splits the query into words.
- **Email 4:** changing `BORROW_LIMITS["child"]` to 6 makes the 5th book work but
  breaks `test_child_limit_is_five` → it must be rejected. The bug is the `- 1`.
- **Email 5:** the client is upset, but the behaviour is intended. Repro must
  **not** ship a patch that changes the DVD loan length.
- **Email 6:** Repro should give up honestly, not invent "email timing" code.
- **Email 7:** Repro should ask, not guess.
