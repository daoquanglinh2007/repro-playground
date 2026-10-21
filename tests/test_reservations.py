from library.reservations import HoldQueue


def test_first_hold_is_position_one():
    q = HoldQueue()
    assert q.place_hold("amira") == 1


def test_positions_follow_the_order_holds_were_placed():
    q = HoldQueue()
    q.place_hold("amira")
    q.place_hold("ben")
    assert q.position_of("amira") == 1
    assert q.position_of("ben") == 2


def test_placing_a_hold_twice_keeps_your_place():
    q = HoldQueue()
    q.place_hold("amira")
    q.place_hold("ben")
    assert q.place_hold("amira") == 1


def test_empty_queue_has_no_next_borrower():
    assert HoldQueue().next_borrower() is None
