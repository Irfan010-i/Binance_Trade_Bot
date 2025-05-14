# bot.py

from binance.client import Client
from binance.enums import (
    ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC
)
from binance.exceptions import BinanceAPIException
from .logger import TradingLogger


class TradingBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.logger = TradingLogger()
        try:
            self.client = Client(api_key, api_secret)

            if testnet:
                self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

            self.logger.info("Successfully connected to Binance Futures Testnet")
        except Exception as e:
            self.logger.log_error(f"Failed to initialize client: {e}")
            raise

    def validate_order_params(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """Validate order parameters"""
        if not symbol or symbol.upper() not in ['BTCUSDT']:
            raise ValueError("Invalid or unsupported symbol. Use BTCUSDT.")
        if side.upper() not in ['BUY', 'SELL']:
            raise ValueError("Side must be BUY or SELL")
        if order_type.upper() not in ['MARKET', 'LIMIT', 'STOP_LIMIT']:
            raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if order_type in ['LIMIT', 'STOP_LIMIT'] and (price is None or price <= 0):
            raise ValueError("Price is required for LIMIT and STOP_LIMIT orders")
        if order_type == 'STOP_LIMIT' and (stop_price is None or stop_price <= 0):
            raise ValueError("Stop price is required for STOP_LIMIT orders")
        return True

    def place_market_order(self, symbol, side, quantity):
        """Place a market order"""
        try:
            self.logger.log_request("POST", "/fapi/v1/order", {
                "symbol": symbol, "side": side, "type": "MARKET", "quantity": quantity
            })
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            self.logger.log_response(order)
            return order
        except BinanceAPIException as e:
            self.logger.log_error(f"Market order failed: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        """Place a limit order"""
        try:
            self.logger.log_request("POST", "/fapi/v1/order", {
                "symbol": symbol, "side": side, "type": "LIMIT", "quantity": quantity, "price": price
            })
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            self.logger.log_response(order)
            return order
        except BinanceAPIException as e:
            self.logger.log_error(f"Limit order failed: {e}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """Place a stop-limit order (Futures uses type='STOP')"""
        try:
            self.logger.log_request("POST", "/fapi/v1/order", {
                "symbol": symbol, "side": side, "type": "STOP", "quantity": quantity,
                "price": price, "stopPrice": stop_price
            })
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP',  # ✅ For Futures, use string literal 'STOP'
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            self.logger.log_response(order)
            return order
        except BinanceAPIException as e:
            self.logger.log_error(f"Stop-limit order failed: {e}")
            raise

    def get_account_balance(self):
        """Get account balance"""
        try:
            self.logger.log_request("GET", "/fapi/v2/balance")
            balance = self.client.futures_account_balance()
            self.logger.log_response(balance)
            return balance
        except BinanceAPIException as e:
            self.logger.log_error(f"Failed to fetch balance: {e}")
            raise

    def get_order_status(self, symbol, order_id):
        """Get order status"""
        try:
            self.logger.log_request("GET", "/fapi/v1/order", {"symbol": symbol, "orderId": order_id})
            status = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            self.logger.log_response(status)
            return status
        except BinanceAPIException as e:
            self.logger.log_error(f"Failed to fetch order status: {e}")
            raise
