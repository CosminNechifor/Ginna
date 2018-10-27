from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


from tools import get_token
from handlers import (
    start,
    start_monitoring,
    perform_get_request,
    start_healthcheck_ws,
    echo,
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

    perform_get_request_handler = CommandHandler(
        'perform_get_request',
        perform_get_request,
    )

    check_ws_periodically = CommandHandler(
        'hc_ws',
        start_healthcheck_ws,
        pass_job_queue=True,
    )

    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_monitoring_handler)
    dispatcher.add_handler(perform_get_request_handler)
    dispatcher.add_handler(check_ws_periodically)

    updater.start_polling()
