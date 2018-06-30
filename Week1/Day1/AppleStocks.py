def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('More number of values required')

    min_price=stock_prices[0]
    max_profit=stock_prices[1]-stock_prices[0]

    for i in xrange(1,len(stock_prices)):
        temp_profit=stock_prices[i]-min_price
        max_profit=max(max_profit,temp_profit)
        min_price=min(min_price,stock_prices[i])

    return max_profit