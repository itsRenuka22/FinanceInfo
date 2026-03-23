import pandas_datareader.data as web
from datetime import datetime, timedelta

while True:
    symbol = input("Please enter a symbol: ").strip()
    if not symbol:
        break

    try:
        end = datetime.today()
        start = end - timedelta(days=7) 

        df = web.DataReader(symbol.upper(), 'stooq', start, end)

        if df.empty or len(df) < 2:
            print(f"Invalid symbol or insufficient data for '{symbol}'.\n")
            continue

        df = df.sort_index()  
        price = df['Close'].iloc[-1]
        prev_close = df['Close'].iloc[-2]
        change = price - prev_close
        change_pct = (change / prev_close) * 100

        now = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        change_str = f"+{change:.2f}" if change >= 0 else f"{change:.2f}"
        pct_str = f"+{change_pct:.2f}%" if change_pct >= 0 else f"{change_pct:.2f}%"

        print(now)
        print(f"{symbol.upper()}")
        print(f"{price:.2f} {change_str} ({pct_str})\n")

    except Exception as e:
        print(f"Error retrieving data: {e}\n")
