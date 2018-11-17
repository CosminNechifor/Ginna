from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters


from tools import get_token
from handlers import (
    start,
    start_monitoring,
    perform_get_request,
    start_healthcheck_ws,
    stop_healthcheck_ws,
    save_note, 
    read_note, 
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

    handler_stop_healthcheck_ws = CommandHandler(
        'stop_hc_ws',
        stop_healthcheck_ws,
        pass_job_queue=True,
    )

    write_note_handler = CommandHandler(
        'note',
        save_note,
    )
    read_note_handler = CommandHandler(
        'note',
        save_note,
    )

    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(write_note_handler)
    dispatcher.add_handler(read_note_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_monitoring_handler)
    dispatcher.add_handler(perform_get_request_handler)
    dispatcher.add_handler(check_ws_periodically)
    dispatcher.add_handler(handler_stop_healthcheck_ws)

    updater.start_polling()
