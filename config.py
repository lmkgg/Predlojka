import os
from dotenv import load_dotenv
import logging

# Загрузка переменных окружения
load_dotenv()

# Telegram Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables")

# Admin Configuration
ADMIN_IDS_STR = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = [int(id_str.strip()) for id_str in ADMIN_IDS_STR.split(",") if id_str.strip()]

# Moderator Configuration
MODERATOR_CODE = os.getenv("MODERATOR_CODE", "qweewq")

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///data/news_bot.db")

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Вывод информации о загрузке конфигурации
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Configuration loaded successfully")
logger.info(f"Admins: {ADMIN_IDS}")
logger.info(f"Database: {DATABASE_URL}")
