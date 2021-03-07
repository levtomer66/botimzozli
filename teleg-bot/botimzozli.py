#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.utils.helpers import escape_markdown
from telegram.ext import Updater
from telegram.ext import MessageHandler, CommandHandler, Filters
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import random
PORT = int(os.environ.get('PORT', 5000))


cloudinary.config(
  cloud_name = "dreemf8x7",
  api_key = "197291118427542",
  api_secret = "2HUZJZvE27YftiBjNVfpgEqKgxM"
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('שלח פה תמונות ולא לזיין יותר מדי את המוח בבקשה')

def incoming_message_action_text(update, context):
    random_texts = ["בוא לא תזיין תשכל ותשלח תמונות, אין לי עצבים אלייך היום","שמע יכלב היה לי יום ארוך אני מציע שתזדיין לי מהקבוצה","בלי הודעות מה לא ברור? בלי הודעות רק תמונות, ובלי דיקפיקס לא רוצה לראות תזין המסריח שלכם","חלאסססססססססססס יראש עבאדי שלח תמונה או שתקבל קיק","אתה יודע מה אתה? נכון אתה על הזין" ]
    update.message.reply_text(random.choice(random_text))

def incoming_message_action_photo(update, context):
    try:
        logging.info (update.message.chat.username)
        file_obj = context.bot.get_file(update.message['photo'][-1]['file_id'])
        file_uri = file_obj.file_path
        file_id = file_obj.file_unique_id
        logging.info(f"Message received: {update.message.chat.username} - [{file_uri}]")
        cloudinary.uploader.upload(file_uri,
            folder = "bots/botimzozli/",
            public_id = file_id,
            overwrite = False,
            resource_type = "image")
        context.bot.send_message(chat_id=update.message.chat_id, text="העלתי סתכל: https://botimzozli.vercel.app/ עוד משהו יהומו?")
    except:
        context.bot.send_message(chat_id=update.message.chat_id, text="משהו קרה ולא הצחלתי לעלות ת'תמונה, כנראה תקוע לי איזה זין איפשהו, שסומר או עציץ יבדקו בלוגים")


def main() -> None:
    # Create the Updater and pass it your bot's token.
    TOKEN = "1556697629:AAFQxfBWMxe6ZT6GfbxW3ZtYBr_y-PRj-NA"
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    incoming_message_text = MessageHandler(Filters.text, incoming_message_action_text)
    incoming_message_photo = MessageHandler(Filters.photo, incoming_message_action_photo)

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://botimzozli-bot.herokuapp.com/' + TOKEN)

    dispatcher.add_handler(incoming_message_text)
    dispatcher.add_handler(incoming_message_photo)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
