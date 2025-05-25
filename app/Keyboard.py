from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton


catalog=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Магазин',url='https://www.youtube.com/',callback_data='t-shirt')],
    [InlineKeyboardButton(text='Инструмент',callback_data='sneakers')],
    [InlineKeyboardButton(text='О нас',callback_data='cap')]])