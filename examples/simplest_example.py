from tianguix.order_book import OrderBook, Order, Side

# Create an order book
book = OrderBook("AMXL")

# Step 1: Add a bid order
print("### Adding a Bid Order: 100 shares @ $18.13 ###")
book.add_order(Order(size=100, price=18.13, side=Side.BID, sender="TraderA"))
print(book.get_order_book_str())

# Step 2: Add an offer order that matches the bid
print("\n### Adding a Matching Offer Order: 100 shares @ $18.13 ###")
book.add_order(Order(size=100, price=18.13, side=Side.ASK, sender="TraderB"))
print(book.get_order_book_str())

