from tianguix.order_book import OrderBook, Bid, Offer

# Create an order book
book = OrderBook()

# Step 1: Add a bid order
print("### Adding a Bid Order: 100 shares @ $18.13 ###")
book.add_order(Bid("A", "AMXL", 100, 18.13))
print(book.get_order_book_str())

# Step 2: Add an offer order that matches the bid
print("\n### Adding a Matching Offer Order: 100 shares @ $18.13 ###")
book.add_order(Offer("B", "AMXL", 100, 18.13))
print(book.get_order_book_str())

# Step 3. Match the orders
print(book.match_orders())
print("\n### Now the book should be empty again ###")
print(book.get_order_book_str())
