from library.catalogue import Item, search_titles

ITEMS = [Item("1", "The Night Garden", "book"), Item("2", "Garden Birds", "dvd")]


def test_search_ignores_case():
    assert [i.item_id for i in search_titles(ITEMS, "night GARDEN")] == ["1"]


def test_search_single_word_finds_every_match():
    assert [i.item_id for i in search_titles(ITEMS, "garden")] == ["1", "2"]
