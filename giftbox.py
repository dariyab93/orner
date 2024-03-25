import telebot
from threading import Timer
import re
from config import BEARER_TOKEN
from main import send_message


# Initialize your Telegram bot
bot = telebot.TeleBot(BEARER_TOKEN)

# Define the function to handle user input during gift box sign-up
def sign_up_for_gift_box(message):
    # Send the initial message to the user
    bot.send_message(message.chat.id, "Привіт! Щоб оформити підписку на подарункову коробку, поділіться, будь ласка, своїм номером телефону.")
    # Set a timer for 3 minutes to send a reminder if the user hasn't responded
    Timer(180, send_reminder, args=[message.chat.id]).start()
    # Set the state to expect phone number input next
    bot.register_next_step_handler(message, process_phone_number)

# Function to send a reminder after 3 minutes
def send_reminder(chat_id):
    bot.send_message(chat_id, "Здається, щось пішло не так. Продовжимо оформлення підписки? 🎁 Поділіться, будь ласка, своїм номером телефону.")
    # Schedule another reminder after 2 hours if the user still hasn't responded
    Timer(7200, send_two_hour_reminder, args=[chat_id]).start()

# Function to send a reminder after 2 hours
def send_two_hour_reminder(chat_id):
    bot.send_message(chat_id, "Ви забули про підписку? 🥺 Зробіть усього декілька кліків і ми почнемо збирати для вас секретний бокс!")
    # Schedule the final message after an additional time
    Timer(7200, send_final_message, args=[chat_id]).start()

# Function to send the final message
def send_final_message(chat_id):
    bot.send_message(chat_id, "Ми більше не будемо турбувати вас нагадуваннями, проте із нетерпінням чекатимемо вашого повернення. Завжди тут 💞")

# Function to handle phone number input
def process_phone_number(message):
    # Save the phone number from the user's message
    phone_number = message.text
    # Validate the phone number (not implemented here)
    # If the phone number is valid, proceed to ask for the recipient's name
    bot.send_message(message.chat.id, "Тепер, будь ласка, вкажіть своє ім'я.")
    # Set the state to expect name input next
    bot.register_next_step_handler(message, process_name)

# Function to handle name input
def process_name(message):
    # Save the first name from the user's message
    first_name = message.text
    # Prompt the user for their last name
    bot.send_message(message.chat.id, "А також прізвище.")
    # Set the state to expect last name input next
    bot.register_next_step_handler(message, process_last_name, first_name)

# Function to handle last name input
def process_last_name(message, first_name):
    # Save the last name from the user's message
    last_name = message.text
    # Prompt the user for their address
    bot.send_message(message.chat.id, "Щоб ми могли доставити бокс Новою поштою, нам потрібна ваша адреса.\n\nБудь ласка, вкажіть населений пункт 👇🏻")
    # Set the state to expect address input next
    bot.register_next_step_handler(message, process_address, first_name, last_name)

# Function to handle address input
def process_address(message, first_name, last_name):
    # Save the address from the user's message
    address = message.text
    # Prompt the user for the first payment
    bot.send_message(message.chat.id, "Вже майже все 🙃 Для завершення оформлення підписки здійсніть, будь ласка, свою першу оплату")
    # Set the state to expect payment confirmation next
    bot.register_next_step_handler(message, process_payment_confirmation, first_name, last_name, address)

# Function to handle payment confirmation
def process_payment_confirmation(message, first_name, last_name, address):
    # Proceed to confirm the subscription
    bot.send_message(message.chat.id, f"Дякуємо, {first_name} {last_name}! Ви успішно підписалися на подарункову коробку!")

