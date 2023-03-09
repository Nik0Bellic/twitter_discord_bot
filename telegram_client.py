from logging import Handler, getLevelName
import requests


class TelegramHandler(Handler):

    def emit(self, record):
        """
        Emit a record.
        If the stream was not opened because 'delay' was specified in the
        constructor, open it before calling the superclass's emit.
        """
        telegram_bot_sendtext(record)


def telegram_bot_sendtext(bot_message):

    bot_token = '2139562951:AAGhli4q15Dx5VIq1l-0Lz38D4B1VB-tYpM'
    bot_chatID = "@bot_test_kaka"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message.msg

    response = requests.get(send_text)
    return response.json()