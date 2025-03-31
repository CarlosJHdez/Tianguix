from enum import Enum
import time

# tianguix/order_book.py


class Side(Enum):
    BID = "Bid"  # Buy Side, represented by B
    ASK = "Ask"  # Sell Side, represented by A
    
    def __str__(self):
        return 'B' if self == Side.BID else 'A'


class Order:
    """Represents an order in the order book."""

    def __init__(self, size, price, side):
        self.size = size  # Size or quantity of the order
        self.price = price  # Price, assumed all prices are on the same currency.
        self.side = side  # Side of the order (BID or ASK)
        self.timestamp = int(time.time_ns())  # Timestamp in nanoseconds when the order was created for this order book.
        self.sequence = None  # Renamed from order_id

    def __repr__(self):
        return f"Order(size={self.size}, price={self.price}, side={self.side}, sequence={self.sequence})"

    def __str__(self):
        return f"Order: {self.side} {self.size} @ {self.price} (Sequence: {self.sequence})"

    def to_html(self):
        return f"""
        <div class="order">
            <span>Side: {self.side}</span><br>
            <span>Size: {self.size}</span><br>
            <span>Price: {self.price}</span><br>
            <span>Sequence: {self.sequence}</span>
        </div>
        """


class Trade:
    """Represents a trade executed in the order book."""

    def __init__(self, bid_sequence, ask_sequence, size, price):
        self.bid_sequence = bid_sequence
        self.ask_sequence = ask_sequence
        self.timestamp = timestamp=int(time.time_ns()),
        self.size = size
        self.price = price

    def __repr__(self):
        return f"Trade(size={self.size}, price={self.price}, bid_seq={self.bid_sequence}, ask_seq={self.ask_sequence})"

    def __str__(self):
        return f"Trade: {self.size} @ {self.price} (Bid Seq: {self.bid_sequence}, Ask Seq: {self.ask_sequence})"

    def to_html(self):
        return f"""
        <div class="trade">
            <span>Size: {self.size}</span><br>
            <span>Price: {self.price}</span><br>
            <span>Bid Sequence: {self.bid_sequence}</span><br>
            <span>Ask Sequence: {self.ask_sequence}</span>
        </div>
        """


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
        """Returns a formatted string representation of the order book with enhanced pretty-printing."""
        output = []
        output.append("\n" + "╔" + "═" * 38 + "╗")
        output.append(f"║ {'BIDS':<10} │ {'PRICE':^10} │ {'OFFERS':>10} ║")
        output.append("╠" + "═" * 10 + "╪" + "═" * 10 + "╪" + "═" * 10 + "╣")

        # Collect all unique prices from bids and offers
        bid_prices = {bid.price: bid.size for bid in self.bids}
        offer_prices = {offer.price: offer.size for offer in self.offers}
        all_prices = sorted(
            set(bid_prices.keys()).union(set(offer_prices.keys())), reverse=True
        )

        for price in all_prices:
            bid_str = f"{bid_prices[price]}" if price in bid_prices else "-"
            offer_str = f"{offer_prices[price]}" if price in offer_prices else "-"
            output.append(f"║ {bid_str:<10} │ {price:^10.2f} │ {offer_str:>10} ║")

        output.append("╚" + "═" * 10 + "╧" + "═" * 10 + "╧" + "═" * 10 + "╝")
        return "\n".join(output)

    def __repr__(self):
        return f"OrderBook(instrument_id={self.instrument_id}, bids={len(self.bids)} offers={len(self.offers)})"

    def __str__(self):
        return f"OrderBook for Instrument ID {self.instrument_id} with {len(self.bids) + len(self.offers)} orders"

    def to_html(self):
        bids_html = "".join(bid.to_html() for bid in self.bids)
        offers_html = "".join(offer.to_html() for offer in self.offers)
        return f"""
        <div class="order-book">
            <h2>OrderBook for Instrument ID {self.instrument_id}</h2>
            <div class="bids">
                <h3>Bids</h3>
                {bids_html}
            </div>
            <div class="offers">
                <h3>Offers</h3>
                {offers_html}
            </div>
        </div>
        """
