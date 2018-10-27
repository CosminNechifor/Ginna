import os


def check_server(bot, job):
    chat_id, hosts = job.context[0], job.context[1]
    for hostname in hosts:
        response = os.system("ping -c 1 " + hostname)
        if response != 0:
            bot.send_message(
                chat_id=chat_id,
                text=f"{hostname} IS DOWN",
            )
