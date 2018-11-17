import requests
import logging


from jobs import (
    check_server,
    check_ws,
)
from tools import (
    save_to_notes,
    read_from_notes,
)

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
    ''' start_monitoring <server1> <server2>...'''
    logger.info('Start monitoring was called')
    bot.send_message(
        chat_id=update.message.chat_id,
        text='I started the monitoring process.',
    )
    # replace this part with regex
    message_text = update.message.text[18:].split(' ')
    context = (update.message.chat_id, message_text)
    job_queue.run_repeating(
        check_server,
        interval=3,
        first=0,
        context=context,
    )


def perform_get_request(bot, update):
    '''Command: /perform_get_request <endpoint>'''
    logger.info('Perform request was called')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Performing request",
    )
    url = update.message.text[21:].split(' ')
    url = url[0]
    r = requests.get(url)
    # this can be replaced, but for the moment it returns only the status code
    response_message = f'Status code: {r.status_code}\n'
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message,
    )


def start_healthcheck_ws(bot, update, job_queue):
    '''
        Epects the ip/url to the ping endpoints
        command: /hc_ws <webs1> <webs2> <webs3>
    '''

    logger.info('Checking web services called')
    # TODO: replace this part with regex
    message_text = update.message.text[7:].split(' ')
    context = (update.message.chat_id, message_text)
    job_queue.run_repeating(
        check_ws,
        interval=3,
        first=0,
        context=context,
    )


def stop_healthcheck_ws(bot, update, job_queue):
    '''
        Stops the WS healthcheck
    '''
    logger.info('Stoping WS healthcheck')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Stoping ws"
    )
    for job in job_queue.get_jobs_by_name('check_ws'):
        job.schedule_removal()


def save_note(bot, update):
    logger.info('Adding to you notes')
    bot.send_message(
        chat_id=update.message.chat_id,
        text='I added what you asked in notes.',
    )
    message_text = update.message.text[6:]
    save_to_notes(message_text)


def read_note(bot, update):
    logger.info('Reading your notes')    
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Printing notes'
    )
    notes_text = read_from_notes() 
    bot.send_message(
        chat_id=update.message.chat_id,
        text=notes_text,
    )