# track-stock-python
A simple Python script to fetch the latest stock price for a given ticker symbol using the Yahoo Finance API via the `yfinance` library. This program allows users to input any stock ticker symbol (e.g., AAPL, MSFT, TSLA) and returns the last available market price for that stock.

## Features

- Fetches the latest stock price for a user-provided ticker symbol.
- Handles both uppercase and lowercase inputs for ticker symbols.
- Includes error handling for cases where data cannot be retrieved (e.g., network issues, invalid ticker symbols).
- Displays a helpful message if no data is found for the entered symbol.

## Prerequisites

- **Python 3.6 or higher** is required.
- **yfinance** library for accessing Yahoo Finance data.

You can install the `yfinance` library using the following command:
```bash

pip install yfinance

Clone this repository or download the script file.

Run the script from your terminal or command prompt:

bash
Copy code
python main.py
Enter the stock ticker symbol when prompted (e.g., AAPL for Apple Inc., MSFT for Microsoft).

The script will output the last market price for the entered stock ticker.
