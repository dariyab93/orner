import typing as t
from telebot import types

# Function to build reply markup
def build_reply_markup(
    button_list: t.Iterable[str],
    one_time_keyboard: bool = True,
    row_width: int = 2,
    resize_keyboard: bool = True) -> types.ReplyKeyboardMarkup:
    """Builds a reply markup for the bot.

    Args:
        button_list (tuple[str]):
            A tuple of strings. Each string is a button.
        one_time_keyboard (bool, optional):
            Whether the keyboard is one-time. Defaults to True.
        row_width (int, optional):
            Number of buttons in a row. Defaults to 2.
        resize_keyboard (bool, optional):
            Flag to resize the keyboard. Defaults to True.

    Returns:
        types.ReplyKeyboardMarkup: The reply markup.
    """
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=resize_keyboard,
        row_width=row_width,
    )
    buttons = [types.KeyboardButton(i) for i in button_list]
    markup.add(*buttons)
    return markup