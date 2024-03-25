import telebot
from message_handler import handle_all_messages
from utils import build_reply_markup
from config import BEARER_TOKEN, MAIN_SCREEN_BUTTON


bot = telebot.TeleBot(BEARER_TOKEN)

@bot.message_handler(commands=["start"])
def start(message) -> None:
    markup = build_reply_markup(MAIN_SCREEN_BUTTON)
    bot.send_message(
        message.chat.id,
        "Ласкаво просимо! Будь ласка, оберіть один із наступних варіантів:",
        reply_markup=markup,
    )

@bot.message_handler(func=lambda message: True)
def handle_all_messages_wrapper(message):
    handle_all_messages(bot, message.text)

# Start polling
bot.polling(none_stop=True)
