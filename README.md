# Sportsbooks moneylines and arbitrage
This application scrapes sports betting websites and analyzes them to find arbitrage opportunities. Arbitrage opportunities are defined as positions where profit is risk-free (i.e. no matter the outcome of the match, the bettor profits). These occur when moneylines on different sites vary, usually due to recent news and slow update times. 

## The following sites are scraped:

-betus.com
-bovada.com
-fanduel.com
-betnow.eu

We use MongoDB and Pymongo to manage incoming data. The database information in this repository DOES NOT link to a working database. In order to use this application, a MongoDB database must be set up.

### Packages Used:

-Scrapy
-pymongo
-dnspython
