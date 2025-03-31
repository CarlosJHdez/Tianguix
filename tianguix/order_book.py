from enum import Enum
import time

# tianguix/order_book.py


class Side(Enum):
    BID = "Bid"
    ASK = "Ask"
    NONE = "None"


class Order:
    """Represents an order in the order book."""

    def __init__(self, size, price, side):
        self.size = size
        self.price = price
        self.side = side
        self.ts_event = int(time.time_ns())
        self.sequence = None  # Renamed from order_id

    def __str__(self):
        return f"Order({self.side}{self.size} @{self.price})"


class Trade:
    """Represents a trade executed in the order book."""

    def __init__(self, bid_sequence, ask_sequence, size, price):
        self.bid_sequence = bid_sequence
        self.ask_sequence = ask_sequence
        self.timestamp = timestamp=int(time.time_ns()),
        self.size = size
        self.price = price

    def __str__(self):
        return f"Trade(size={self.size} @ price={self.price})"


class OrderBook:
    """Maintains lists of bids and offers and matches trades."""

    def __init__(self, instrument_id):
        self.instrument_id = instrument_id  # Add instrument_id attribute
        self.bids = []
        self.offers = []
        self.executed_trades = []
        self._next_sequence = 1  # Renamed from _next_order_id
        

    def add_order(self, order):
        """Adds a bid or offer to the order book."""
        order.sequence = self._next_sequence  # Renamed from order_id
        self._next_sequence += 1  # Renamed from _next_order_id

        if order.side == Side.BID:
            self.bids.append(order)
            self.bids.sort(key=lambda x: x.price, reverse=True)  # Highest price first
        elif order.side == Side.ASK:
            self.offers.append(order)
            self.offers.sort(key=lambda x: x.price)  # Lowest price first
            
        return order.sequence

    def match_orders(self):
        """Matches bids and offers based on price and size."""
        while self.bids and self.offers and self.bids[0].price >= self.offers[0].price:
            bid = self.bids[0]
            offer = self.offers[0]
            trade_size = min(bid.size, offer.size)

            trade = Trade(
                bid_sequence=bid.sequence,
                ask_sequence=offer.sequence,
                
                size=trade_size,
                price=offer.price,
            )
            self.executed_trades.append(trade)

            # Update sizes or remove orders if fully matched
            bid.size -= trade_size
            offer.size -= trade_size
            if bid.size == 0:
                self.bids.pop(0)
            if offer.size == 0:
                self.offers.pop(0)

        return self.executed_trades

    def get_order_book_str(self):
        """Returns a formatted string representation of the order book with three columns: Bids, Price, Offers."""
        output = []
        output.append("\n" + "=" * 40)
        output.append(f"{'BIDS':<10} | {'PRICE':^10} | {'OFFERS':>10}")
        output.append("=" * 40)

        # Collect all unique prices from bids and offers
        bid_prices = {bid.price: bid.size for bid in self.bids}
        offer_prices = {offer.price: offer.size for offer in self.offers}
        all_prices = sorted(
            set(bid_prices.keys()).union(set(offer_prices.keys())), reverse=True
        )

        for price in all_prices:
            bid_str = f"{bid_prices[price]}" if price in bid_prices else "-"
            offer_str = f"{offer_prices[price]}" if price in offer_prices else "-"
            output.append(f"{bid_str:<10} | {price:^10.2f} | {offer_str:>10}")

        output.append("=" * 40)
        return "\n".join(output)
