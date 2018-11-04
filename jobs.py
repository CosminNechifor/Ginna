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
        try:
            response = requests.get(h)
            # TODO: To better handle responses
            code = response.status_code
            if code == 200:
                pass
        except Exception:
            bot.send_message(
                chat_id=chat_id,
                text=f'Page does not exist or Internal server error: {h}',
            )
