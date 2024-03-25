# Function to handle user messages
import re
import requests
from order_status import get_order_status
from order_search import search_order
from responses import get_order_response
from main import send_message
from config import BEARER_TOKEN


def handle_message(message):
    if message == "Отримати статус замовлення":
        prompt_for_order_details()
    elif message == "Підписатися на подарункову коробку":
        sign_up_for_gift_box()
    else:
        # Check if the message is a valid phone number
        if re.match(r'^\d{10}$', message):
            order_id = search_order_by_phone(message)
            if order_id:
                status = get_order_status(order_id, BEARER_TOKEN)
                if status:
                    send_message(f"Статус замовлення: {status}")
        else:
            # Assuming the message is a tracking number
            order_id = search_order_by_tracking(message)
            if order_id:
                status = get_order_status(order_id, BEARER_TOKEN)
                if status:
                    send_message(f"Статус замовлення: {status}")

def prompt_for_order_details():
    send_message("Будь ласка, введіть свій номер телефону або номер відстеження.")

def sign_up_for_gift_box():
    send_message("Ви успішно підписалися на подарункову коробку! Дякуємо!")

def send_message(message):
    print(message)  


