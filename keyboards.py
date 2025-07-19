from pyrogram.types import ReplyKeyboardMarkup

import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.profile_button, buttons.rating_button],
        [buttons.setting_button],
    ],
    resize_keyboard=True,
)

setting_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.sign_up_button, buttons.back_button],
    ],
    resize_keyboard=True,
)