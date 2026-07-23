# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable stocks:")
for stock in stock_prices:
    print(f"{stock}: ${stock_prices[stock]}")

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        print(f"✅ {stock_name}: {quantity} shares × ${price} = ${investment}")

    except ValueError:
        print("❌ Please enter a valid number.")

print("\n================================")
print(f"💰 Total Investment: ${total_investment}")