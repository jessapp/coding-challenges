# I grabbed Apple's stock prices from yesterday and put them in an array called stockPrices, where:

# The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
# The values are the price (in US dollars) of one share of Apple stock at that time.
# So if the stock cost $500 at 10:30am, that means stockPrices[60] = 500.

# Write an efficient method that takes stockPrices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

# No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.

  def get_max_profit(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError


    min_price = stock_prices_yesterday[0]

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for price in stock_prices_yesterday[1:]:
        potential_profit = price - min_price

        max_profit = max(max_profit, potential profit)

        min_price = min(min_price, price)


    return max_profit