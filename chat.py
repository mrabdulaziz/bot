import telebot
import time
bot = telebot.TeleBot('')
CHAT = ''
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, 'Напишите нам вопрос или свои пожелания', )
@bot.message_handler(commands=['help'])
def help_handler(message):
    bot.send_message(message.from_user.id, 'Вы можете отправить ваши контакные данные и ваши жалобы')
@bot.message_handler(func=lambda message:True)
def forward_handler(message):
    try:
        if message.chat.id == int(CHAT):
            bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            bot.forward_message(CHAT, message.chat.id, message.message_id)

    except Exception as error:
        print("Exception in forward handler. Info: {}".format(error))
    print(message)
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(15)

