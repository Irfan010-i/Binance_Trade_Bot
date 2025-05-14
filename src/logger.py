import logging
import os
from datetime import datetime

class TradingLogger:
    def __init__(self, log_file='logs/trading_bot.log'):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def log_request(self, method, endpoint, params=None):
        self.info(f"API Request: {method} {endpoint} | Params: {params}")

    def log_response(self, response):
        self.info(f"API Response: {response}")

    def log_error(self, error):
        self.error(f"Error: {str(error)}")