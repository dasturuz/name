from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


but = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ariza kiritish ✍️")
        ]
    ],
    resize_keyboard=True
)
but2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash 👌"),
            KeyboardButton(text="Bekor Qilish ❌")
        ]
    ],
    resize_keyboard=True
)