import click
import os
from .bot import TradingBot
from .logger import TradingLogger

@click.group()
def cli():
    """Binance Futures Trading Bot CLI"""
    pass

@cli.command()
@click.option('--api-key', required=True, help='Binance API Key')
@click.option('--api-secret', required=True, help='Binance API Secret')
def init(api_key, api_secret):
    """Initialize the trading bot"""
    logger = TradingLogger()
    try:
        bot = TradingBot(api_key, api_secret, testnet=True)
        logger.info("Trading bot initialized successfully")
        click.echo("Trading bot initialized successfully")
    except Exception as e:
        logger.log_error(f"Initialization failed: {e}")
        click.echo(f"Error: {e}", err=True)

@cli.command()
@click.option('--symbol', default='BTCUSDT', help='Trading pair (e.g., BTCUSDT)')
@click.option('--side', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), required=True, help='Order side')
@click.option('--quantity', type=float, required=True, help='Order quantity')
def market_order(symbol, side, quantity):
    """Place a market order"""
    logger = TradingLogger()
    try:
        bot = TradingBot(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_SECRET_KEY'), testnet=True)
        order = bot.place_market_order(symbol, side, quantity)
        click.echo(f"Market Order Placed: {order}")
    except Exception as e:
        logger.log_error(f"Market order failed: {e}")
        click.echo(f"Error: {e}", err=True)

@cli.command()
@click.option('--symbol', default='BTCUSDT', help='Trading pair (e.g., BTCUSDT)')
@click.option('--side', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), required=True, help='Order side')
@click.option('--quantity', type=float, required=True, help='Order quantity')
@click.option('--price', type=float, required=True, help='Limit price')
def limit_order(symbol, side, quantity, price):
    """Place a limit order"""
    logger = TradingLogger()
    try:
        bot = TradingBot(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_SECRET_KEY'), testnet=True)
        order = bot.place_limit_order(symbol, side, quantity, price)
        click.echo(f"Limit Order Placed: {order}")
    except Exception as e:
        logger.log_error(f"Limit order failed: {e}")
        click.echo(f"Error: {e}", err=True)

@cli.command()
@click.option('--symbol', default='BTCUSDT', help='Trading pair (e.g., BTCUSDT)')
@click.option('--side', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), required=True, help='Order side')
@click.option('--quantity', type=float, required=True, help='Order quantity')
@click.option('--price', type=float, required=True, help='Limit price')
@click.option('--stop-price', type=float, required=True, help='Stop price')
def stop_limit_order(symbol, side, quantity, price, stop_price):
    """Place a stop-limit植物 order"""
    logger = TradingLogger()
    try:
        bot = TradingBot(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_SECRET_KEY'), testnet=True)
        order = bot.place_stop_limit_order(symbol, side, quantity, price, stop_price)
        click.echo(f"Stop-Limit Order Placed: {order}")
    except Exception as e:
        logger.log_error(f"Stop-limit order failed: {e}")
        click.echo(f"Error: {e}", err=True)

@cli.command()
def balance():
    """Check account balance"""
    logger = TradingLogger()
    try:
        bot = TradingBot(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_SECRET_KEY'), testnet=True)
        balance = bot.get_account_balance()
        click.echo(f"Account Balance: {balance}")
    except Exception as e:
        logger.log_error(f"Balance check failed: {e}")
        click.echo(f"Error: {e}", err=True)

@cli.command()
@click.option('--symbol', default='BTCUSDT', help='Trading pair (e.g., BTCUSDT)')
@click.option('--order-id', type=int, required=True, help='Order ID')
def order_status(symbol, order_id):
    """Check order status"""
    logger = TradingLogger()
    try:
        bot = TradingBot(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_SECRET_KEY'), testnet=True)
        status = bot.get_order_status(symbol, order_id)
        click.echo(f"Order Status: {status}")
    except Exception as e:
        logger.log_error(f"Order status check failed: {e}")
        click.echo(f"Error: {e}", err=True)

if __name__ == '__main__':
    cli()