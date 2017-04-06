  def get_max_profit(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError


    min_price = stock_prices_yesterday[0]

    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for time, price in enumerate(stock_prices_yesterday):
        if time == 0:
            continue

        potential_profit = price - min_price

        max_profit = max(max_profit, potential profit)

        min_price = min(min_price, price)


    return max_profit