# tests/test_order_book.py
import pytest
from tianguix.order_book import OrderBook, Order, Side

INSTRUMENT_ID  = 2

def test_order_simple_execution():
    book = OrderBook(INSTRUMENT_ID)
    bid = Order(size=100, price=18.13, side=Side.BID)
    offer = Order(size=100, price=18.13, side=Side.ASK)

    book.add_order(bid)
    book.add_order(offer)

    trades = book.match_orders()
    assert len(trades) == 1
    assert trades[0].size == 100
    assert trades[0].price == 18.13
    assert trades[0].bid_sequence == bid.sequence
    assert trades[0].ask_sequence == offer.sequence

def test_order_at_least_two_orders():
    book = OrderBook(INSTRUMENT_ID)
    bid1 = Order(size=100, price=18.13, side=Side.BID)
    bid2 = Order(size=100, price=18.13, side=Side.BID)
    offer = Order(size=200, price=18.13, side=Side.ASK)

    book.add_order(bid1)
    book.add_order(bid2)
    book.add_order(offer)

    trades = book.match_orders()
    assert len(trades) == 2
    assert trades[0].size == 100
    assert trades[0].price == 18.13
    assert trades[0].bid_sequence == bid1.sequence
    assert trades[0].ask_sequence == offer.sequence

    assert trades[1].size == 100
    assert trades[1].price == 18.13
    assert trades[1].bid_sequence == bid2.sequence
    assert trades[1].ask_sequence == offer.sequence
