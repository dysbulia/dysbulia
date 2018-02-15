from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
import requests



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Working.')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


"""
def coin(bot, update):
    update.message.reply_text("In progress")

    coinname = update.message.text
    coinsplit = coinname.split()
    justcoin = coinsplit[-1]

    with open("../data_scraper/data/" + justcoin + ".csv", 'r') as f:
         lastrow = None
         for lastrow in csv.reader(f):pass

    marketcap = lastrow.marketcap
    volume = lastrow.exchangevolume
    price = lastrow.price

    update.message.reply_text(justcoin + "price: " + price + justcoin +
                              "volume: " + volume + justcoin +
                              "marketcap: " + marketcap)
                              """


def coin(bot, update):
    update.message.reply_text("In progress")

    coinname = update.message.text
    coinsplit = coinname.split()
    cn = coinsplit[-1]
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/' + cn)
    for cn in r.json():

        update.message.reply_text(cn["name"] + " Rank: " + cn["rank"])
        update.message.reply_text("Price USD: " + cn["price_usd"])
        update.message.reply_text("Price BTC: " + cn["price_btc"])
        update.message.reply_text("24h Volume: " + cn["24h_volume_usd"])
        update.message.reply_text("Marketcap: " + cn["market_cap_usd"])

        if float(cn["percent_change_1h"]) >= 0:
            update.message.reply_text("% Change 1H: " + cn["percent_change_1h"] + " 🔺")

        else:
            update.message.reply_text("% Change 1H: " + cn["percent_change_1h"] + " 🔻")

        if float(cn["percent_change_24h"]) >= 0:
            update.message.reply_text("% Change 24H: " + cn["percent_change_24h"] + " 🔺")
        else:
            update.message.reply_text("% Change 24H: " + cn["percent_change_24h"] + " 🔻")

        if float(cn["percent_change_7d"]) >= 0:
            update.message.reply_text("% Change 7D: " + cn["percent_change_7d"] + " 🔺")
        else:
            update.message.reply_text("% Change 7D: " + cn["percent_change_7d"] + " 🔻")





def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("514520114:AAGpSfP5D2aKYHqYIEiasLQu-3Rjs86azJA")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("coin", coin))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

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