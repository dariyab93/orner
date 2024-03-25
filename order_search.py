import requests

# Function to search for order by identifier (phone number or tracking number)
def search_order(identifier):
    api_url = "https://orner.com.ua/api/v1/public/order/search"
    params = {
        "search": identifier,
        "page": 1,
        "size": 10
    }
    response = requests.post(api_url, params=params)
    if response.status_code == 200:
        order_data = response.json()
        if order_data:
            orders = order_data.get('orders', [])
            if orders:
                order_id = orders[0]['order']['id']
                return order_id
    print(f"Failed to search for order by identifier: {identifier}")
    return None