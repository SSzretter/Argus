import asyncio
import sys
import logging
import traceback
import argus
from argus.app import bot, db, engine, logger
from argus.config import config

# Faster Event Loop
try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

logger.info(f"Starting Argus: {argus.__version__}")
bot.db = db
bot.engine = engine


def main():
    try:
       # asyncio.run(bot.run(config["bot"]["token"], log_handler=None))
        bot.run(config["bot"]["token"], log_handler=None)
    except (KeyboardInterrupt, SystemExit, RuntimeError):
        logger.info(f"Shutting Down Argus")
    except Exception as e:
        logger.error(traceback.format_exc())
    finally:
        sys.exit()


if __name__ == "__main__":
    main()
