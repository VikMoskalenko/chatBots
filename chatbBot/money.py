import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6828743258:AAFGLBm95FqNIuaOFNXfcZQl_4MPjNIwM3c')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, enter the number')
    bot.register_next_step_handler(message, sum)
    
def sum(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'wrong enter')
        bot.register_next_step_handler(message, sum)
        return
    if amount > 1: 
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Else', callback_data='else')
    
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id, 'Choose the currency', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Number should be bigger than one')
        bot.register_next_step_handler(message, sum)
    
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"You`ve got {round(res, 2)}, you can start from scratch")
        bot.register_next_step_handler(call.message, sum)
    else:
        bot.send_message(call.message.chat.id, 'Enter some definitions using slash')
        bot.register_next_step_handler(call.message, my_currency)
    
def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"You`ve got {round(res, 2)}, you can start from scratch")
        bot.register_next_step_handler(message, sum)
    except Exception:
        bot.send_message(message.chat.id, "Something went wrong. Try again later.")
        bot.register_next_step_handler(message, my_currency)
    
    
bot.polling(none_stop=True)