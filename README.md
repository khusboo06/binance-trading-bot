# Binance Futures Trading Bot (Testnet)

## Setup

pip install -r requirements.txt

Add API keys in `.env`

## Run

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 30000

## Features
- Market & Limit orders
- BUY / SELL
- CLI interface
- Logging
- Error handling

## Logs
Check app.log file