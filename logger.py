import logging
from telegram_client import TelegramHandler, telegram_bot_sendtext


log = logging

# Set default log settings
log_level = 'INFO'
log_file = 'bot.log'

send_telegram = True

if send_telegram:
    log.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    handlers=[logging.FileHandler(log_file), logging.StreamHandler(), TelegramHandler()])
else:
    log.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    handlers=[logging.FileHandler(log_file), logging.StreamHandler()])

logger = logging.getLogger(__name__)
level = logging.getLevelName(log_level)
logger.setLevel(level)