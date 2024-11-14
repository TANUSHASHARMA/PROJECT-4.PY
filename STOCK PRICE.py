import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch stock price from Alpha Vantage API
def get_stock_price():
    stock_symbol = entry.get().upper()
    api_key = 'your_alpha_vantage_api_key'  # Replace with your actual API key

    # Make API request
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stock_symbol,
        'interval': '1min',  # You can choose another interval like '5min', '15min', etc.
        'apikey': api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if 'Time Series (1min)' in data:
            # Get the latest time and corresponding price
            latest_time = next(iter(data['Time Series (1min)']))
            latest_price = data['Time Series (1min)'][latest_time]['1. open']
            label_result.config(text=f"Latest Price for {stock_symbol}: ${latest_price}")
        else:
            messagebox.showerror("Error", "Unable to fetch data for this symbol. Please check the stock symbol and try again.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("Stock Price Tracker")

# Label for the title
label_title = tk.Label(root, text="Stock Price Tracker", font=("Arial", 16))
label_title.pack(pady=10)

# Entry widget for stock symbol input
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Button to fetch stock price
button_fetch = tk.Button(root, text="Get Stock Price", font=("Arial", 14), command=get_stock_price)
button_fetch.pack(pady=10)

# Label to display the result
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Start the main loop for the GUI
root.mainloop()
