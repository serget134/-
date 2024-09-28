import telebot
import requests

bot = telebot.TeleBot('7871759619:AAHw74CS9IvPJ0xBNz-r_sAy0Ypkh21jKmk')

start_txt = 'Привет! Это бот прогноза погоды. \n\nОтправьте боту название города и он скажет, какая там температура.'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])

def weather(message):
  city = message.text
  url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
  weather_data = requests.get(url).json()
  print(weather_data)
  temperature = round(weather_data['main']['temp'])
  w_now = 'Сейчас в городе ' + city + ' ' + str(temperature) + ' °C'
  bot.send_message(message.from_user.id, w_now)
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e: 
            print('Что-то не то')