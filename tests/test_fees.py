from datetime import date

from library.fees import days_late, late_fee

DUE = date(2026, 3, 2)


def test_on_time_is_free():
    assert late_fee(DUE, DUE) == 0


def test_days_late_never_negative():
    assert days_late(DUE, date(2026, 3, 1)) == 0


def test_five_days_late_is_charged_for_every_day():
    assert late_fee(DUE, date(2026, 3, 7)) == 100


def test_fee_is_capped():
    assert late_fee(DUE, date(2026, 5, 1)) == 500
