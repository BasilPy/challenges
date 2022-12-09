import requests
import telebot
# import PyTelegramBotAPI
import tokens
from datetime import datetime
url_sheety_choir = tokens.URL_sheety_choir
token = tokens.TOKEN
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'a'])
# /start and /a messages
def send_welcome(message):
    bot.reply_to(message, "Type your name:")

@bot.message_handler(commands=['check'])
# /check messages
def send_welcome(message):
    sheet_response0 = requests.get(url_sheety_choir)
    #data0 = sheet_response0.json()["sheet1"]
    #print(data0)
    bot.reply_to(message, sheet_response0.text)



today_date = datetime.today().strftime('%d.%m.%Y')
now_time = datetime.now().strftime('%H')
# input_name = "Artyom Aspednikov"
#
# input_name = "Nadya Sutormina"
# data = {
#         "sheet1": {
#             "date": today_date,
#             "part": now_time,
#             "name": input_name,
#         }
# }

#sheet_response = requests.get(url_sheety_choir)
#data = sheet_response.json()["sheet1"]
# print(data)
# for i in data:
#     last_id = i["id"]
#     last_date = i["date"]
# print(last_date)
# print(last_id)
# print(data)
@bot.message_handler(content_types=['text'])
def send_echo(message):
    data = {
        "sheet1": {
            "date": today_date,
            "part": now_time,
            "name": message.text,
        }
    }
    sheet_responseP = requests.post(url_sheety_choir, json=data)
    bot.send_message(message.chat.id, sheet_responseP.text)

bot.polling(none_stop = True)

# sheet_responseP = requests.post(url_sheety_choir, json=data)
# print(sheet_responseP.text)
# print(now_time)
# print(data)


