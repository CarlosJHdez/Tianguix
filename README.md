# Tianguix
Tianguix is the implementation of an order book as used on a financial market.

An order book is at the heart of any market, whether flowers, financial, or anything.


The idea behind it is to concentrate the interest of buyers and sellers by aggregating their orders (or interest) in firm orders (the other being a quotation market, which can take a similar form)


The idea is that transactions on a particular instrument (financial, like a stock, or something like a kind of entrance for a theather) can be aggregated in two ordered lists, one for buyers and one for sellers.


Each list has the size (amount of the particular instrument willing to transact) and the price (at which the buyer or seller is willing to close the transaction. Additional attributes can be added to represent priority (two orders with the same price will be fullfilled FIFO in time, i.e. first to come in time will be filled first)


For a bit of formality, lets suppose we have two lists:
B = {b1, b2, …, bn} where bi represents someone that wants to buy bi.size at bi.prize
S = {s1, s2, ... , sn} where si represents someone that wants to sell s1. At s1 prize.


This abstraction allows to represent multiple transaction models. A few examples


Auction.


On an auction, a lot of size M is distributed amongst the highest bidders on a list. On this case the Auction is represented as:
B = {b1, b2, .. , bn}
S = empty
And after a period of time, M is distributed amongts the first elements of B ordered by prize where sum(bi… bm) = M


Continuous Market


On a continuous market, each time that b1.price >= s1.price, a transaction between b1 and s1 at s1 price.






Stock Market


A collection of order books, each one with an allocation method (Auction, Continuous Market) for a particular type of stock.


Ticket market


A collection of order books, each one with an allocation method, for each kind of seat on the theather.

