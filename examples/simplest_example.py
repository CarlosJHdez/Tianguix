from tianguix.order_book import OrderBook, Order, Side

# Create an order book
book = OrderBook("AMXL")

# Step 1: Add a bid order
print("### Adding a Bid Order: 100 shares @ $18.13 ###")
book.add_order(Order(size=100, price=18.13, side=Side.BID))
print(book.get_order_book_str())

# Step 2: Add an offer order that matches the bid
print("\n### Adding a Matching Offer Order: 100 shares @ $18.13 ###")
book.add_order(Order(size=100, price=18.13, side=Side.ASK))
print(book.get_order_book_str())

# Step 3. Match the orders
print(book.match_orders())
print("\n### Now the book should be empty again ###")
print(book.get_order_book_str())

# Step 4. Add two bid orders of the same size
print("\n### Adding Two Bid Orders: 100 shares @ $18.12 ###")
book.add_order(Order(size=100, price=18.12, side=Side.BID))
book.add_order(Order(size=100, price=18.12, side=Side.BID))
print(book.get_order_book_str())

# Step 5. Add one offer order that matches the bid.
print("\n### Adding a Matching Offer Order: 100 shares @ $18.12 ###")
book.add_order(Order(size=100, price=18.12, side=Side.ASK))
print(book.get_order_book_str())

# Step 6. Match the orders
print(book.match_orders())
print("\n### Now the book should be empty again ###")
print(book.get_order_book_str())

