import os
import sys

import telebot

from config import TOKEN
from version import VERSION, NEW


class DogBot(telebot.TeleBot):
    excited = False
    pets = 0


DOG = DogBot(TOKEN)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = BASE_DIR + '/images/'


@DOG.message_handler(commands=['start', 'help'])
def send_welcome(message):
    DOG.send_message(
        message.chat.id,
        "~Dog bot barks at " +
        message.chat.first_name +
        " welcomingly~"
    )


@DOG.message_handler(commands=['pet'])
def pet(message):
    DOG.pets += 1
    if DOG.pets == 1:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You barely lifted your hand and Lesser Dog got excited."
        )
    elif DOG.pets == 2:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You lightly touched the Dog. It's already overexcited..."
        )
    elif DOG.pets == 3:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You pet the Dog. It raises its head up to meet your hand."
        )
    elif DOG.pets == 4:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You pet the Dog. It was a good Dog."
        )
    elif DOG.pets == 5:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Lesser Dog is overstimulated."
        )
    elif DOG.pets == 6:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You pet the Dog. Its excitement knows no bounds."
        )
    elif DOG.pets == 7:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Critical pet! Dog excitement increased."
        )
    elif DOG.pets == 8:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You have to jump up to pet the Dog."
        )
    elif DOG.pets == 9:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You don't even pet it. It gets more excited."
        )
    elif DOG.pets == 10:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Lesser Dog shows no signs of stopping."
        )
    elif DOG.pets == 11:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "There is no way to stop this madness."
        )
    elif DOG.pets == 12:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Lesser Dog enters the realm of the clouds."
        )
    elif DOG.pets == 13:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "You call the Dog but it is too late. It cannot hear you."
        )
    elif DOG.pets == 14:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "It's possible that you may have a problem."
        )
    elif DOG.pets == 15:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Lesser Dog is learning to read."
        )
    elif DOG.pets == 16:
        DOG.send_photo(
            message.chat.id,
            open(IMG_DIR + str(DOG.pets)+'.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Lesser Dog is questioning your choices."
        )
    else:
        DOG.send_photo(
            message.chat.id,
            open('images/17.png', 'rb')
        )
        DOG.send_message(
            message.chat.id,
            "Really..."
        )


@DOG.message_handler(commands=['spare'])
def version(message):
    DOG.send_message(
        message.chat.id,
        "Lesser Dog Found A Loving Owner."
    )
    DOG.pets = 0


@DOG.message_handler(commands=['version'])
def version(message):
    DOG.send_message(
        message.chat.id,
        "Version: {0}\nWhat's New:{1}".format(VERSION, NEW)
    )


DOG.polling()

