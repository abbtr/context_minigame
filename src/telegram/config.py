from dotenv import load_dotenv
import logging
import os

load_dotenv()

class AppConfig:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    WEBHOOK_URL_BASE = os.getenv("WEBHOOK_URL_BASE")
    DATABASE_URL = os.getenv("DATABASE_URL")

    def configure_logging(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )


app_config = AppConfig()