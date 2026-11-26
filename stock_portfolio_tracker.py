import csv

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 170.00,
    "AMZN": 190.00,
}


def get_positive_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity > 0:
                return quantity
        except ValueError:
            pass

        print("Enter a positive whole number, such as 5.")


def save_csv(holdings, total):
    filename = "portfolio.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Stock",
            "Quantity",
            "Price per share",
            "Investment value",
        ])

        for symbol, quantity in holdings.items():
            price = STOCK_PRICES[symbol]
            value = price * quantity
            writer.writerow([symbol, quantity, f"{price:.2f}", f"{value:.2f}"])

        writer.writerow(["TOTAL", "", "", f"{total:.2f}"])

    print(f"Portfolio saved to {filename}.")


def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")

    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f} per share")

    print("\nEnter stock symbols and quantities. Type DONE when finished.")

    holdings = {}

    while True:
        symbol = input("Stock symbol: ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("That stock is not in the price list.")
            continue

        quantity = get_positive_quantity(f"Quantity of {symbol}: ")
        holdings[symbol] = holdings.get(symbol, 0) + quantity

    if not holdings:
        print("No stocks entered.")
        return

    print("\nPortfolio summary:")
    total = 0.0

    for symbol, quantity in holdings.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        print(f"  {symbol}: {quantity} shares × ${price:.2f} = ${value:.2f}")

    print(f"Total investment: ${total:.2f}")

    choice = input("Save the summary to a CSV file? (y/n): ").strip().lower()

    if choice == "y":
        save_csv(holdings, total)
    else:
        print("Summary not saved.")


if __name__ == "__main__":
    main()