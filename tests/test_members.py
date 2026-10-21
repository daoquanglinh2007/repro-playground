import pytest

from library.members import Member


def test_new_member_can_borrow():
    assert Member("amira").can_borrow()


def test_child_limit_is_five():
    assert Member("ben", kind="child").limit == 5


def test_member_at_the_limit_cannot_borrow():
    m = Member("carl", kind="child", on_loan=["a", "b", "c", "d", "e"])
    with pytest.raises(ValueError):
        m.borrow("f")
