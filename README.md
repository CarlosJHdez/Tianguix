# Tianguix

**Tianguix** aims to be a "marketplace in a box"- a one-stop shop for all the essential infrastructure needed to create a marketplace. Initially, I envisioned it as just an order book, but adding a few more features will make it useful and more fun to write.  

Marketplaces come in many forms, but the two most relevant to me are:  
- **Simple auctions**  
- **Continuous two-sided (buyer/seller) auctions**  

At the same time, marketplaces require certain features to be workable in today's infrastructure. Below is a wishlist of capabilities that I would like to see in a "marketplace in a box":  
- A **flexible yet simple order book** with an intuitive interface and limited (no pun intended) but effective order-matching options.  
- An **auction book** supporting [English and Dutch auctions](https://en.wikipedia.org/wiki/Auction).
- A simple mechanism to send orders to the exchange and, in general, to get the state of the order, perhaps taking the best spirit of the FIX protocol but removing the accumulated cruft to leave the actual spirit of the transaction.
- **Reliable market data distribution**, ideally compact and fast, similar to what financial exchanges provide.
All of the above should be able to be used through a REST interface, as crypto exchanges do now, but with a solid, specific transaction core.

### Big *NOs*
I haven't seen how crypto exchanges are implemented, but I pray to Olympus that it is not just a regular messaging service. Certainly, Tianguix can be simple, but it should not just rely on REST protocols.
- Big no to Native FIX protocol implementations.
- I will add things as they pop. 

## Key Features  

- **Algorithmic flexibility**: While the initial implementation will be in Python (as it’s my strongest language), the design should allow multiple language implementations while maintaining computational efficiency, where we can always copy what we know works, particularly the use of binary trees to give constant complexity to the most common operations. (More to be worked here, of course)
- **Single-threaded books/auctions**: The current standard in most markets is a single-threaded process where orders are added in a time-based or first-come, first-served manner. This aligns with how most major exchanges operate today. 
- **Deployment options**:  
  - A modular, **dockable architecture** for easy deployment as a functional exchange.  
  - **Seamless testing and back-testing capabilities**, ensuring ease of simulation and validation.  

## The Core Idea  

### The Order book 

`tianguix.orderbook` implements an order book as it is used in financial markets.  

I would like to be able to see this sequence executed cleanly 

At its core, an **order book** centralizes buyers' and sellers' interests by aggregating their firm orders (as opposed to a quotation-based market, which may operate differently).  

Transactions for a specific instrument (e.g., a stock or concert ticket) can be structured into two ordered lists:  
- **Buyers** list (demand)  
- **Sellers** list (supply)  

Each order contains:  
- **Size**: The quantity of the instrument to be transacted.  
- **Price**: The price at which the buyer or seller is willing to execute the trade.  
- **Priority**: (Impliciti) Orders at the same price are filled on best-price first, then  **FIFO (first-in, first-out)** basis, meaning the earliest order takes precedence.  

This foundation serves as the basis for auctions and order book mechanics.

---



# Order Book Example: Basic Trade Execution  

## **1. Placing Orders**  
Two participants enter the market:  

- **A** places a **buy order** for **100 AMXL shares** at **$18.13**.  
- **B** places a **sell order** for **100 AMXL shares** at **$18.13**.  

## **2. Order Matching & Execution**  
A trade is executed since the buy and sell orders match in both **quantity** and **price**.  

## **3. Execution Report**  
Both **A** and **B** receive an execution report confirming:  

- **100 shares traded** at **$18.13**.  
- The orders are now fulfilled.  

## **Python Code Example (Using `tianguix.order_book`)**
```python
from tianguix.order_book import OrderBook, Bid, Offer

# Initialize the order book
order_book = OrderBook()

# Create bid and offer
bid = Bid(id="A", symbol="AMXL", quantity=100, price=18.13)
offer = Offer(id="B", symbol="AMXL", quantity=100, price=18.13)

# Submit orders to the book
order_book.add_order(bid)
order_book.add_order(offer)

# Process matching and generate execution report
executions = order_book.match_orders()

# Print execution reports
for execution in executions:
    print(f"Execution Report: {execution.quantity} {execution.symbol} @ {execution.price} for {execution.buyer} and {execution.seller}")
```
