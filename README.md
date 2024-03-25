# Orner chatbot 

---

# Telegram Bot for tracking orders or signing up for gift subscriptions through Orner 
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
- `main.py`: Main script containing the bot implementation.
- `config.py`: Configuration file for storing sensitive information such as API tokens.
- `test_main.py`: Unit tests for testing the functionality of the bot.
- `your_module.py`: Placeholder for any additional modules or functions used by the bot.

## Testing
To run the unit tests:
```
python -m unittest test_main.py
```

## Contributing
Contributions are welcome! If you'd like to contribute to the project, feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README according to your project's specific requirements and features.
