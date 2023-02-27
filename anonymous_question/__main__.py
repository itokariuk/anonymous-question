import logging

from aiogram import Bot, Dispatcher

from anonymous_question import config


logging.basicConfig(
    format="%(asctime)s - %(name)s- %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Application entry point"""

    bot = Bot(token=config.TELEGRAM_BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.run_polling(bot)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
