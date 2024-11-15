import yfinance as yf

# Prompt the user to enter the stock ticker symbol
ticker_symbol = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ")

try:
    # Download data for the entered ticker symbol
    data = yf.download(ticker_symbol, period='1d', interval='1d')
    
    # Check if data is retrieved and not empty
    if not data.empty:
        last_market_price = data['Close'].iloc[-1]
        print(f"Last market price for {ticker_symbol.upper()}: ${last_market_price}")
    else:
        print(f"No data found for {ticker_symbol.upper()}. It might be delisted or unavailable.")

except Exception as e:
    print(f"Failed to retrieve data for {ticker_symbol.upper()}: {e}")
