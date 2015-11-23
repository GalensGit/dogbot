import os

import telebot

from config import TOKEN
from version import VERSION, NEW

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = BASE_DIR + '/images/'

class DogBot(telebot.TeleBot):
    excited = False
    pets = 0    


dog = DogBot(TOKEN)


@dog.message_handler(commands=['start', 'help'])
def send_welcome(message):
    import pdb; pdb.set_trace()
    dog.send_message(
        message.chat.id,
        "~Dog bot barks at " +
        message.chat.first_name +
        " welcomingly~"
    )


@dog.message_handler(commands=['pet'])
def pet(message):
    dog.pets += 1
    if dog.pets == 1:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You barely lifted your hand and Lesser Dog got excited."
        )
    elif dog.pets == 2:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You lightly touched the Dog. It's already overexcited..."
        )
    elif dog.pets == 3:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You pet the Dog. It raises its head up to meet your hand."
        )
    elif dog.pets == 4:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You pet the Dog. It was a good Dog."
        )
    elif dog.pets == 5:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Lesser Dog is overstimulated."
        )
    elif dog.pets == 6:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You pet the Dog. Its excitement knows no bounds."
        )
    elif dog.pets == 7:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Critical pet! Dog excitement increased."
        )
    elif dog.pets == 8:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You have to jump up to pet the Dog."
        )
    elif dog.pets == 9:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You don't even pet it. It gets more excited."
        )
    elif dog.pets == 10:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Lesser Dog shows no signs of stopping."
        )
    elif dog.pets == 11:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "There is no way to stop this madness."
        )
    elif dog.pets == 12:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Lesser Dog enters the realm of the clouds."
        )
    elif dog.pets == 13:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "You call the Dog but it is too late. It cannot hear you."
        )
    elif dog.pets == 14:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "It's possible that you may have a problem."
        )
    elif dog.pets == 15:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Lesser Dog is learning to read."
        )
    elif dog.pets == 16:
        dog.send_photo(
            message.chat.id,
            open(IMG_DIR + str(dog.pets)+'.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Lesser Dog is questioning your choices."
        )
    else:
        dog.send_photo(
            message.chat.id,
            open('images/17.png', 'rb')
        )
        dog.send_message(
            message.chat.id,
            "Really..."
        )


@dog.message_handler(commands=['spare'])
def version(message):
    dog.send_message(
        message.chat.id,
        "Lesser Dog Found A Loving Owner."
    )
    dog.pets = 0


@dog.message_handler(commands=['version'])
def version(message):
    dog.send_message(
        message.chat.id,
        "Version: {0}\nWhat's New:{1}".format(VERSION, NEW)
    )


dog.polling()

