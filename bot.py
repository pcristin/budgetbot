import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Привет, мой дорогой Друг! Я буду помогать вести тебе твой бюджет ! Введи сумму, которую хочешь накопить')
	


def help(update, context):
	"""Send a message when the command /help is issued."""
	#над текстом этого сообщения надо будет потом вместе подумать
	update.message.reply_text("Помощь")

def currentState(update, context):
	"""Takes current state and visualisate it via diagramm"""
	update.message.reply_text("На текущмй момент вы накопили n рублей из N. Затраты на текущий месяц составили:")

def generalCategories(update, context):
	"""User sees general categories and answering about theirs' usage"""
	reply_markup = ReplyKeyboardMarkup([['Да', 'Нет']], one_time_keyboard=True)
	update.message.reply_text("Хотите использовать предложенные категории?(Да/нет)", reply_markup=reply_markup)

def customizeCategories(update, context):
	"""If user chooses own categories"""
	update.message.reply_text("Введите категории, которые хотите использовать")


def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater("1174316531:AAEzc_EpFprCwSXMufThTmJEB6Jl7MHbHOo", use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("state", currentState))
	dp.add_handler(CommandHandler("categories", generalCategories))
	dp.add_handler(CommandHandler("edit_categories", customizeCategories))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	main()