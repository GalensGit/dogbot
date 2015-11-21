import time
from config import *
from version import *
import telebot


# dog = telebot.TeleBot(TOKEN)


class DogBot(telebot.TeleBot):
    excited = False
    pets = 0


dog = DogBot(TOKEN)


@dog.message_handler(commands=['start', 'help'])
def send_welcome(message):
    dog.send_message(
        message.chat.id,
        "~Dog bot barks at " + message.chat.first_name + " welcomingly~"
    )


@dog.message_handler(commands=['pet'])
def pet(message):
    dog.pets += 1
    if dog.pets == 1:
        dog.send_photo(
            message.chat.id,
            open('images/'+str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You barely lifted your hand and Lesser Dog got excited."
        )


@dog.message_handler(commands=['version'])
def version(message):
    dog.send_message(
        message.chat.id,
        "Version: {0}\nWhat's New:{1}".format(VERSION, NEW)
    )

dog.polling()

