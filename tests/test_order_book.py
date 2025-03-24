# tests/test_order_book.py
import pytest
from tianguix.order_book import OrderBook, Bid, Offer


def test_order_execution():
    book = OrderBook()
    bid = Bid("A", "AMXL", 100, 18.13)
    offer = Offer("B", "AMXL", 100, 18.13)

    book.add_order(bid)
    book.add_order(offer)

    trades = book.match_orders()
    assert trades == [("A", "B", "AMXL", 100, 18.13)]
