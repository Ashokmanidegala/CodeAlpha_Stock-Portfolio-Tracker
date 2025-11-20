stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 120, "MSFT": 310}

portfolio = {}
total_value = 0

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not found in price list.")

for stock, qty in portfolio.items():
    total_value += stock_prices[stock] * qty

print("\nPortfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock]*qty}")

print(f"\nTotal Investment Value: ${total_value}")

with open("portfolio.txt", "w") as file:
    file.write("Stock,Quantity,Price,Total\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
    file.write(f"Total,,,{total_value}\n")


print("\nPortfolio saved to 'portfolio.txt'")
