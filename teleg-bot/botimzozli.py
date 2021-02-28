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
    update.message.reply_text('Hi!')


def help_command(update: Update, context) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def incoming_message_action(update, context):
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


    if True:
        context.bot.send_message(chat_id=update.message.chat_id, text="Download completed!")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Download NOT possible!")


def inlinequery(update: Update, context) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(), title="Caps", input_message_content=InputTextMessageContent(query.upper())
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"*{escape_markdown(query)}*", parse_mode=ParseMode.MARKDOWN
            ),
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"_{escape_markdown(query)}_", parse_mode=ParseMode.MARKDOWN
            ),
        ),
    ]

    update.inline_query.answer(results)


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("1556697629:AAFQxfBWMxe6ZT6GfbxW3ZtYBr_y-PRj-NA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    incoming_message = MessageHandler(Filters.photo, incoming_message_action)

    dispatcher.add_handler(incoming_message)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
