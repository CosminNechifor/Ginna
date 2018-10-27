import logging

from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

from jobs import check_server
from tools import get_token


# setting up logging so that we know if things are breaking
# where did they break
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def start(bot, update):
    logger.info('start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hi there, I'm Ginna",
    )


def echo(bot, update):
    logger.info('echo')
    bot.send_message(
        chat_id=update.message.chat_id,
        text=update.message.text,
    )


def start_monitoring(bot, update, job_queue):
    logger.info('Start monitoring was called')
    # replace this part with regex
    message_text = update.message.text[18:].split(' ')
    message_text.remove('')
    context = [update.message.chat_id, message_text]
    job_queue.run_repeating(
        check_server,
        interval=3,
        first=0,
        context=context,
    )


if __name__ == '__main__':

    token = get_token()

    updater = Updater(
        token=token,
        workers=10,
    )
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    start_monitoring_handler = CommandHandler(
        'start_monitoring',
        start_monitoring,
        pass_job_queue=True,
    )

    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_monitoring_handler)

    updater.start_polling()
    # updater.stop()
