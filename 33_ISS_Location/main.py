import requests
from datetime import datetime
import telebot  # install PyTelegramBotAPI

bot = telebot.TeleBot("5875564867:AAGY8PLVwrGwvx6GxZNNwD8r")  # Token is changed


@bot.message_handler(commands=['start', 'help'])
# /start and /help messages
def send_welcome(message):
    bot.reply_to(message, "Type /check to find out location of ISS:")


# MY_LAT = 43.222015
# MY_LONG = 76.851250
MY_LAT = 5
MY_LONG = -45
UP_LAT = MY_LAT + 5
DOWN_LAT = MY_LAT - 5
UP_LONG = MY_LONG - 5
DOWN_LONG = MY_LAT - 5
iss_lat = 0.0
iss_long = 0.0


def is_iss_overhead():
    # checking the position of ISS. is in visible for our location?
    global iss_long, iss_lat
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    if DOWN_LAT < iss_lat < UP_LAT and DOWN_LONG < iss_long < UP_LONG:
        return True
    else:
        return False


# print(f" {longitude}\n {latitude}")


def is_night():
    # Sun rize and Sunset. We can see ISS only at night ˆ_ˆ
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    # print(sunrise)
    # print(sunset)
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0]) - 15  # London time
    sunset_hour = int(sunset.split("T")[1].split(":")[0]) - 15
    time_now_hour = datetime.now().hour
    if sunrise_hour <= time_now_hour <= sunset_hour:
        return False
    else:
        return True


@bot.message_handler(commands=['check'])
# /check, returns latitude and longitude of ISS, and whether we can see it or not
def send_info(message):
    if is_night() and is_iss_overhead():
        bot.reply_to(message, f"ISS latitude = {iss_lat},\nlongitude = {iss_long},\n YOU CAN SEE ISS!")
    else:
        bot.reply_to(message, f"ISS latitude = {iss_lat},\nlongitude = {iss_long},\n You can't see it :(")


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, "done")
    bot.stop_bot()


bot.infinity_polling(timeout=10)



