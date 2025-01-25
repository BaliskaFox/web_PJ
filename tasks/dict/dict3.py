prices = {"яблоко": 100, "банан": 200, "вишня": 300}
for key in prices:
    prices[key] += int(prices[key] * 0.1)
print(new_prices = {key: int(value * 1.1) for key, value in prices.items()})
print(prices)