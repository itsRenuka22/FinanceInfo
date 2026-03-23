# FinanceInfo

A CLI tool that displays stock price and daily change for a given ticker symbol.

## Setup

```bash
pip3 install pandas_datareader
```

## Usage

```bash
python3 FinanceInfo.py
```

Enter a stock symbol (e.g. `AAPL`) when prompted. Press Enter with no input to quit.

## Notes

- Data is sourced from Stooq
- Price change is calculated relative to the previous trading day's close
