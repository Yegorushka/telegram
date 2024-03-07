import telebot
token = '6881031942:AAGFGnOEFqnzrexoDYokCaDPCq3P5jm5Sus'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()