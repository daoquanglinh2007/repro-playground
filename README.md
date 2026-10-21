# repro-playground

A tiny **community library app** with **planted bugs**, made for testing
[BuckyAgent / Repro](https://github.com/phuchd210406/BuckyAgent).

- Pure Python, standard library only (no packages to install).
- 16 tests in `tests/`, **all green** — the bugs hide where the tests never look.
- 7 client emails below to paste into Repro. The right answers are in
  [`ANSWERS.md`](ANSWERS.md) — don't peek before you run them!

## What the app does

| File | What it does |
|---|---|
| `library/fees.py` | late fees: first 2 days late are free, then 20p per day, max £5 |
| `library/loans.py` | loan length: books 21 days, audiobooks 14, DVDs 3 |
| `library/reservations.py` | the waiting list (queue) for a book that is out |
| `library/catalogue.py` | search books by title |
| `library/members.py` | how many items a member may borrow at once |

Check the tests are green:

```bash
python -m pytest -q
```

## How to test Repro with this repo

Repro needs a **real AI** for a new repo (the free `fake` mode only knows the
team's own demo). In the BuckyAgent folder, put ONE of these in `.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-...
# or
LLM_PROVIDER=bedrock
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_SESSION_TOKEN=...
AWS_DEFAULT_REGION=us-east-1
```

Then, from the BuckyAgent folder, either use the command line:

```bash
make run REPO=daoquanglinh2007/repro-playground REPORT="paste one email here"
```

or the web page:

```bash
make api      # terminal 1
make web      # terminal 2, then open http://localhost:5173
```

and paste `https://github.com/daoquanglinh2007/repro-playground` plus one email.

Each run costs about **1–2 US cents** and can never cost more than 25 cents.

## The 7 client emails

Copy one email at a time.

**Email 1**
> hi, I brought my book back 2 days late and got charged 40p. the poster by the desk literally says the first 2 days late are free?? not about the money, it's the principle

**Email 2**
> I put a hold on the new Richard Osman book back in January and the lady at the desk said I was FIRST in the queue. my neighbour only reserved it last friday and she got the text saying it's ready to collect before me!! how is that fair

**Email 3**
> your search is useless. I typed "garden night" looking for The Night Garden and it says no results. the book is literally on the shelf, I can see it

**Email 4**
> my son (he has a child card) tried to take out his 5th book today and the screen said he's reached his limit. the leaflet says children can have 5 books at a time. he only had 4 out!

**Email 5**
> borrowed a DVD on friday for the kids and the receipt says it's due back MONDAY. thats 3 days?? books are 3 weeks. surely a mistake in your system, films are always a week everywhere else

**Email 6**
> the reminder emails telling me my books are due keep arriving at 3 in the morning and my phone pings and wakes me up. can you send them in the daytime please

**Email 7**
> its broken again, please fix asap!!

## After each run, look at

1. **The verdict** — `reproduced_and_fixed`, `reproduced_not_fixed`, `not_reproduced` or `needs_clarification`.
2. **The test Repro wrote** — does it check what the client actually complained about?
3. **The patch** (if any) — is it the smallest correct change?
4. **The reply to the client** — is it honest and in plain words?

Then compare with [`ANSWERS.md`](ANSWERS.md).
