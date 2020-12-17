import telebot

from packege.parser import get_stats

bot= telebot.TeleBot('1360131281:AAFC1IwsXys5WrgtMfP4PhBxSdmvviGcDVM')
keyboard = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard.row("/start")

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    if user.username == 'dodikovich':
        bot.send_message(message.chat.id, 'Бог создал горы, Бог создал деревья, Бог создал тебя, но все мы совершаем ошибки.')
    else:
        IKeybord = telebot.types.InlineKeyboardMarkup()
        FORTNITE = telebot.types.InlineKeyboardButton("Fortnite", callback_data="Fortnite")
        CSGO = telebot.types.InlineKeyboardButton("CSGO", callback_data="CSGO")
        IKeybord.add(FORTNITE, CSGO)
        bot.send_message(message.chat.id, 'Привет '+user.first_name+' , выбери игру', reply_markup=IKeybord)
        send_stats()



def send_stats():
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        name = message.text
        bot.send_message(message.chat.id, "it can take several minutes")
        if name:
            get_stats(name, bot, message)


bot.polling()