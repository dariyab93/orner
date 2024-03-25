# Telegram Bot for tracking orders or signing up for gift subscriptions through Orner 
---

## Overview
This project implements a Telegram bot that facilitates the subscription process for a gift box service. Users can interact with the bot to sign up for a gift box subscription, check the status of their orders, and more.

## Features
- **Subscription Process**: Users can sign up for a gift box subscription by providing their phone number, name, address, and completing the payment process.
- **Order Status**: Users can inquire about the status of their orders by providing their order ID.
- **Reminders**: The bot sends reminders to users who haven't completed the subscription process or haven't responded to prompts within a specified timeframe.

## Getting Started
### Prerequisites
- Python 3.x
- Required Python packages (install via `pip`):
  ```
  pip install python-telegram-bot requests
  ```

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/dariyab93/orner.git
   ```
2. Navigate to the project directory:
   ```
   cd orner
   ```
   
### Usage
1. Run the `main.py` script to start the bot:
   ```
   python main.py
   ```
2. Interact with the bot by sending commands and messages in your Telegram chat.

## File Structure
- `main.py`: This script contains the main bot logic and setup.
- `config.py`: Configuration file for storing sensitive information such as the BEARTOKEN.
- `order_status.py`: This script contains the function to retrieve the order status.
- `message_handler.py`: This script contains the logic for handling user messages.
- `order_search.py`: This script contains the function to search for orders by phone number or tracking number.
- `responses.py`: This script contains the function to generate responses based on the order status.
- `utils.py`: This script contains utility functions such as build_reply_markup, which is used for building reply markup buttons.
- `giftbox.py`: A script for handling the "Sign Up for a "Giftbox" option. Takes the user through a series of questions.
- `test_search.py`: Runs some tests on the order_search function 
 

## Testing
To run the unit tests:
```
python -m unittest test_search.py
```

