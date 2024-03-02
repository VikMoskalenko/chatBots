#buttons, text, file

import telebot
from telebot import types 

bot = telebot.TeleBot('460057589:AAG56aTKBAXI9EvykOS826byIhl3J0ToW0g')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('follow the link')
    markup.row(btn1)
    btn2 = types.KeyboardButton('delete')
    btn3 = types.KeyboardButton('change text')
    markup.row(btn2, btn3)
    #sending photo 
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #you can send audio using = bot.send_audio(message.chat.id, file)
    #bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
    
def on_click(message):
    if message.text == 'follow the link':
        bot.send_message(message.chat.id, 'website is open')
    elif message.text == 'delete':
        bot.send_message(message.chat.id, 'deleted')

@bot.message_handler(content_types=['photo', 'image'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('follow the link', url='https://www.youtube.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('delete', callback_data='delete')
    btn3 = types.InlineKeyboardButton('change text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'what a fantastic photo', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id )


bot.polling(none_stop=True)