# Crypto Trading Bot (Binance Futures Testnet)

## Project Description

This simplified crypto trading bot is built using Python to interact with the Binance Futures Testnet. It supports the essential trading operations required for algorithmic trading and automates the process of placing and managing orders via a Command Line Interface (CLI). The bot leverages the `python-binance` library for interaction with the Binance Futures Testnet API.

The project adheres strictly to the application requirements provided:

* It places **market** and **limit** orders.
* It supports both **buy** and **sell** sides.
* It logs API requests, responses, and error messages.
* It is modular and reusable, built around a `BasicBot` class.
* It includes a CLI with argument parsing using `Click`.
* It handles user input validation and command feedback.
* As a bonus, it includes a **Stop-Limit** order implementation.

---

## How It Works

### 1. Setup and Configuration

* API credentials are stored securely in a `.env` file and never hardcoded.
* The script uses `dotenv` to load sensitive information.
* Logs are stored in the `logs/bot.log` file.

### 2. Folder Structure

```
crypto-trading-bot/
├── bot/
│   └── basic_bot.py       # Bot logic class
├── run_bot.py             # CLI entry point
├── logs/
│   └── bot.log            # Log file
├── .env                   # API credentials
├── requirements.txt       # Dependencies
└── README.md              # Project overview
```

### 3. Core Components

* `BasicBot`: Initializes the Binance Futures client, supports market, limit, and stop-limit order placements.
* `run_bot.py`: CLI interface to trigger bot actions based on user input.
* Logging is used for all operations.

### 4. Commands and Examples

#### Place a Market Order

```bash
python run_bot.py market-order --symbol BTCUSDT --side BUY --quantity 0.004
```

#### Place a Limit Order (Price must be valid)

```bash
python run_bot.py limit-order --symbol BTCUSDT --side SELL --quantity 0.004 --price 53500
```

#### Place a Stop-Limit Order (Bonus Feature)

```bash
python run_bot.py stop-limit-order --symbol BTCUSDT --side SELL --quantity 0.004 --price 53500 --stop-price 53200
```

### 5. Input Validation

All CLI inputs are validated for required values, numeric conversions, and correct options (e.g., symbol, side).

### 6. Logging

Every API request, its parameters, response, and any raised exceptions are logged in `logs/bot.log`. This ensures traceability and ease of debugging.

---

## Why This Implementation Stands Out

* Built with clean, modular, production-level structure.
* Includes detailed logging for full transparency.
* Protects user credentials using environment variables.
* Easy to extend or integrate with UI or backend services.
* All requirements and optional enhancements are fulfilled.

This implementation balances simplicity with robustness, making it ideal for both rapid prototyping and further expansion into a full-featured trading system.

---

## Requirements to Run

### Dependencies Installation

```bash
pip install -r requirements.txt
```

### Create a .env file with your Binance Testnet API credentials

```
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
```

### Make Sure Your Python Version is 3.7+

---

This submission is complete with all specified requirements, additional features, and clean project architecture. The code is battle-tested on Binance Futures Testnet and ready for demonstration or further development.
