from pyrogram.types import KeyboardButton
from pyrogram import emoji


back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
profile_button = KeyboardButton(f'{emoji.PERSON} Профиль')
rating_button = KeyboardButton(f'{emoji.CROWN} Рейтинг ')
setting_button = KeyboardButton(f'{emoji.GEAR} Настройки')
sign_up_button = KeyboardButton(f'{emoji.PEN} Регистрация')