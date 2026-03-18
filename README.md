# 🚀 Binance Futures Trading Bot (Testnet)

## 📌 Overview

This is a Python-based CLI trading bot that allows users to place **MARKET** and **LIMIT** orders on Binance Futures Testnet (USDT-M).

The application features a **modern interactive CLI interface**, structured codebase, logging, and error handling.

---

## ✨ Features

* ✅ Interactive CLI (no need to type long commands)
* ✅ Supports BUY and SELL orders
* ✅ Supports MARKET and LIMIT order types
* ✅ Clean and modular code structure
* ✅ Logging of API requests, responses, and errors
* ✅ Input validation and error handling
* ✅ Beautiful terminal UI using `rich`

---

## 🛠 Tech Stack

* Python 3.x
* python-binance
* rich (for modern CLI UI)
* python-dotenv

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py        # Binance client setup
│   ├── orders.py        # Order placement logic
│   ├── validators.py    # Input validation
│   ├── logging_config.py
│
├── cli.py               # Interactive CLI entry point
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
```

⚠️ Use Binance Futures Testnet API keys only
👉 https://testnet.binancefuture.com

---

## ▶️ Usage (Interactive Mode)

Run the application:

```
python cli.py
```

### 🧠 Example Flow:

```
🚀 Binance Trading Bot

Enter Symbol: BTCUSDT
Select Side: BUY / SELL
Select Order Type: MARKET / LIMIT
Enter Quantity: 0.01
Enter Price (if LIMIT): 70000
```

---

## 📊 Output Example

```
📊 Order Result

Symbol        BTCUSDT
Side          BUY
Type          MARKET
Order ID      12345678
Status        NEW
Executed Qty  0.000
Avg Price     0.00
```

---

## 📄 Logs

All logs are stored in:

```
app.log
```

Includes:

* API requests
* API responses
* Errors (if any)

---

## ⚠️ Notes

* This project uses **Binance Futures Testnet** (no real money involved)
* Orders may remain in `NEW` state due to testnet behavior
* LIMIT orders execute only when price conditions are met



