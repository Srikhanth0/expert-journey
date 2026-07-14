import json
import requests

class Portfolio:
    def __init__(self,filename):
        self.filename = filename
        try:
            with open (filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}


    def save_data(self):
        with open (self.filename, 'w') as file:
            json.dump(self.data, file)


    def add_coin(self, amount, ticker):
        if ticker in self.data:
            self.data[ticker] += amount
        else:
            self.data[ticker] = amount

        self.save_data()


    def display_portfolio(self):
        if not self.data:
            print("portfolio is empty")
        else:
            for k,v in self.data.items():
                print(k,v)

    def get_price(self, ticker):
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={ticker}'
        response = requests.get(url).json()
        price = float(response["price"])
        return price

    def calculate_price(self):
        total= 0
        for k,v in self.data.items():
            live_price=self.get_price(k + "USDT")
            total+=live_price*v

        print(total)


# Create the portfolio (this will create 'my_wallet.json' if it doesn't exist)
my_portfolio = Portfolio("my_wallet.json")

# Add some fake coins to test with
my_portfolio.add_coin(0.5, "BTC")
my_portfolio.add_coin(10.0, "ETH")


def user_input():
    enter=int(input("""1.for viewing your portfolio value press (1) \n 2. for calculating live value press (2) \n Enter your choice: """))
    if enter == 1:
        print("--- My Holdings ---")
        my_portfolio.display_portfolio()

    elif enter == 2:
        print("\n--- Total Live Value (USD) ---")
        my_portfolio.calculate_price()

    elif enter >= 3:
        print("Invalid choice")



if __name__ == "__main__":
    user_input()