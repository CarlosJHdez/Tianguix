# Tianguix

**Tianguix** aims to be a "marketplace in a box": offer a one-stop shop for all the essential infrastructure needed to create a marketplace. Initially, I envisioned it as just an order book, but adding a few more features will make it actually useful and more fun to write.  

Marketplaces come in many forms, but the two most relevant to me are:  
- **Simple auctions**  
- **Continuous two-sided (buyer/seller) auctions**  

At the same time, marketplaces require certain features to be workable in today's infrastructure. Below is a wishlist of capabilities that I would like to see in a "marketplace in a box":  
- A **flexible yet simple order book** with an intuitive interface and limited but effective order-matching options.  
- An **auction book** supporting [[English auctions|https://en.wikipedia.org/wiki/Auction]] and Dutch auctions.  
- **Reliable market data distribution**, ideally compact and fast, similar to what financial exchanges provide.  

## Key Features  

- **Algorithmic flexibility**: While the initial implementation will be in Python (as it’s my strongest language), the design should allow multiple language implementations while maintaining computational efficiency, where we can always copy what we know works, particularly the use of binary trees to give constant complexity to the most common operations. (More to be worked here, of course)
- **Single-threaded books/auctions**: The current standard in most markets is a single-threaded process where orders are added in a time-based or first-come, first-served manner. This aligns with how most major exchanges operate today. 
- **Deployment options**:  
  - A modular, **dockable architecture** for easy deployment as a functional exchange.  
  - **Seamless testing and back-testing capabilities**, ensuring ease of simulation and validation.  

## The Core Idea  

Tianguix implements an order book that is used in financial markets.  

At its core, an **order book** centralizes buyers' and sellers' interests by aggregating their firm orders (as opposed to a quotation-based market, which may operate differently).  

Transactions for a specific instrument (e.g., a stock or concert ticket) can be structured into two ordered lists:  
- **Buyers** list (demand)  
- **Sellers** list (supply)  

Each order contains:  
- **Size**: The quantity of the instrument to be transacted.  
- **Price**: The price at which the buyer or seller is willing to execute the trade.  
- **Priority**: Orders at the same price are filled on best-price first, then  **FIFO (first-in, first-out)** basis, meaning the earliest order takes precedence.  

This foundation serves as the basis for auctions and order book mechanics.

---

# Buyers and Sellers in a Marketplace  

## List B: Bids  
**B** = {b₁, b₂, …, bₙ}, where each **bᵢ** represents an individual bid.  

Each buyer has the following attributes:  
- **bᵢ.size**: The quantity they wish to purchase.  
- **bᵢ.price**: The price they are willing to pay.  

## List O: Offers  
**S** = {s₁, s₂, …, sₙ}, where each **sᵢ** represents an individual offer.  

Each seller has the following attributes:  
- **sᵢ.price**: The price at which they are willing to sell.  

This abstraction serves as the starting point for designing auctions and order books.  
