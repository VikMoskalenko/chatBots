# import telebot
# import requests
# import json

# API = '0469851704a849953c63400dc5dc9dc6'

# bot = telebot.TeleBot('6745699780:AAFXbpc7lTIQeb63zyOGSIYOdjXAltz9IJk')

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Hi, nice to meet you! Write down city`s name: ')

# @bot.message_handler(commands=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     if res.status_code == 200:
#         data = json.loads(res.text)
#         temp = data["main"]["temp"]
#         bot.reply_to(message, f'The weather is : {temp}')
    
#         image = 'sunny.png' if temp > 5.0 else 'cloud.jpg'
#         file = open('./' + image, 'rb')
#         bot.send_photo(message.chat.id, file)
#     else:
#         bot.reply_to(message, 'Wrong city name')
    
    
    
# bot.polling(none_stop=True)

import telebot
import requests
import json
import time  

API = '0469851704a849953c63400dc5dc9dc6'

bot = telebot.TeleBot('6745699780:AAFXbpc7lTIQeb63zyOGSIYOdjXAltz9IJk')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi, nice to meet you! Write down city`s name: ')

@bot.message_handler(func=lambda message: True)  # Change to handle all text messages
def get_weather(message):
    # Extract the city name from the message
    city = message.text.strip().lower()

    try:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        res.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        
        bot.reply_to(message, f'The weather is: {temp}')

        image = 'sunny.png' if temp > 5.0 else 'cloud.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OpenWeatherMap API: {e}")
        bot.reply_to(message, 'Error fetching weather information. Please try again later.')

    except json.JSONDecodeError:
        print("Error decoding JSON response from OpenWeatherMap API")
        bot.reply_to(message, 'Error decoding weather information. Please try again later.')

    except KeyError:
        print("Error accessing temperature information in the JSON response")
        bot.reply_to(message, 'Error accessing weather information. Please try again later.')

    except Exception as e:
        print(f"Unexpected error: {e}")
        bot.reply_to(message, 'An unexpected error occurred. Please try again later.')

bot.polling(none_stop=True)
