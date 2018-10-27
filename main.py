import os
import logging

from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


# setting up logging so that we know if things are breaking
# where did they break
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_token():
    path = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(path, 'token.txt')
    token = open(token_path, 'r').read().rstrip()
    return token


def start(bot, update):
    logger.critical('start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please talk to me!",
    )


def echo(bot, update):
    logger.critical('echo')
    bot.send_message(
        chat_id=update.message.chat_id,
        text=update.message.text,
    )


if __name__ == '__main__':

    token = get_token()

    updater = Updater(
        token=token,
    )
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    # updater.stop()
