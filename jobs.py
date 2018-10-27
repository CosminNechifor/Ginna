import os
import requests


def check_server(bot, job):
    chat_id, hosts = job.context
    for hostname in hosts:
        response = os.system("ping -c 1 " + hostname)
        if response != 0:
            bot.send_message(
                chat_id=chat_id,
                text=f'{hostname} IS DOWN',
            )


def check_ws(bot, job):
    chat_id, hosts = job.context
    for h in hosts:
        response = requests.get(h)
        # TODO: To better handle responses
        code = response.status_code
        if code == 200:
            bot.send_message(
                chat_id=chat_id,
                text=f"{h} IS UP",
            )
        elif code == 404:
            bot.send_message(
                chat_id=chat_id,
                text=f'URL:{h} not found',
            )
        # assuming that the other responses will be 500
        else:
            bot.send_message(
                chat_id=chat_id,
                text=f'Internal server error',
            )
