import time
import telebot
import pyTelegramBotAPI

TOKEN = "1938167379:AAELTxSbr3GJHZma12Div9tb9JQDzpeghkY"
bot = telebot.TeleBot(TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '(Do This Task

👉👉Join Telegram Group: @Moon100xToken

👉👉Like Our Facebook page: https://www.facebook.com/107218184991527/posts/107220121658000/

👉👉Follow our Twitter and retweet it: https://twitter.com/Moon100xB/status/1419674879918436356?s=19


You Must Complete All Task . To get airdrop rewards

Press /Start_Airdrop)')

@bot.message_handler(commands=['Start_Airdrop']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'join the telegram server https://t.me/Moon100xToken
Press /Done_telegram_join')

@bot.message_handler(commands=['Done_telegram_join']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Like Our Facebook page: https://www.facebook.com/107218184991527/posts/107220121658000/
Press /Done_fb_like')

@bot.message_handler(commands=['Done_fb_like']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Follow our Twitter and retweet it: https://twitter.com/Moon100xB/status/1419674879918436356?s=19
Press /Done_twitter')


@bot.message_handler(commands=['Your_balance Moon100x : xxx (10$)
Referr to your friend to get xxx m100x (3$) Your Referral Link : https://t.me/Moon100xbot?start=ref01

We will check your referr manually and your task']) # help message handler
def send_welcome(message):
    bot.reply_to(message, '
Press /re_submit_again')



@bot.message_handler(commands=['re_submit_again']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '(Do This Task

👉👉Join Telegram Group: @Moon100xToken

👉👉Like Our Facebook page: https://www.facebook.com/107218184991527/posts/107220121658000/

👉👉Follow our Twitter and retweet it: https://twitter.com/Moon100xB/status/1419674879918436356?s=19


You Must Complete All Task . To get airdrop rewards

Press /Start_Airdrop)')



@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://telegram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)