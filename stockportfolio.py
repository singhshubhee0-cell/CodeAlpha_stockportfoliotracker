#   STOCK PORTFOLIO TRACKER
# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 310,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker ")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# --- Input Section ---
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print("❌ Invalid stock symbol. Please choose from:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid integer for quantity.")
        continue

    # Add to portfolio
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += stock_prices[stock] * quantity

# --- Output Section ---
print("\n Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n Total Investment Value: ${total_investment}")

# --- Optional File Saving ---
save_option = input("\nDo you want to save this summary? (yes/no): ").lower()

if save_option == "yes":
    file_type = input("Save as (txt/csv): ").lower()

    if file_type == "txt":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("------------------------\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(" Portfolio saved as 'portfolio_summary.txt'")

    elif file_type == "csv":
        with open("portfolio_summary.csv", "w") as file:
            file.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
            file.write(f"Total,,,{total_investment}\n")
        print(" Portfolio saved as 'portfolio_summary.csv'")

    else:
        print(" Invalid file type. Data not saved.")