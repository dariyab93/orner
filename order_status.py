# Function to retrieve order status from Orner API
import requests
from config import BEARER_TOKEN

def get_order_status(order_id, BEARER_TOKEN):
    api_url = f'https://orner.com.ua/api/v1/public/order/{order_id}/status'
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        order_data = response.json()
        return order_data.get('status')
    else:
        print("An unexpected error occurred. Please try again later.")
        return None  
   