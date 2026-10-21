from datetime import date

import pytest

from library.loans import due_date


def test_books_are_three_weeks():
    assert due_date("book", date(2026, 3, 2)) == date(2026, 3, 23)


def test_dvd_loans_are_three_days():
    # Policy: DVDs are short loans because there are so few copies.
    assert due_date("dvd", date(2026, 3, 6)) == date(2026, 3, 9)


def test_unknown_kind_is_refused():
    with pytest.raises(ValueError):
        due_date("boardgame", date(2026, 3, 2))
