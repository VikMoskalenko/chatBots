#commands and text
import telebot
import webbrowser

bot = telebot.TeleBot ('460057589:AAG56aTKBAXI9EvykOS826byIhl3J0ToW0g')
#website
@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.google.com.ua')


#fn for user
@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id,f'Hiya {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}') 
    elif message.text.lower() == '/start':
        bot.send_message(message.chat.id,f'Hiya {message.from_user.first_name}')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id,'<b>Help</b> <em><u>information</u></em>', parse_mode='html')
        
#fn to decorate action in bot
@bot.message_handler(commands=['start', 'hello', 'main'])
def main(message):
    bot.send_message(message.chat.id,f'Hiya {message.from_user.first_name}')
    #bot.send_message(message.chat.id, message)
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<b>Help</b> <em><u>information</u></em>', parse_mode='html')

#to run the bot change to true
bot.polling(none_stop=False)