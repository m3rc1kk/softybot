from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🖍️ Adobe Photoshop', callback_data='Adobe Photoshop'), InlineKeyboardButton(text = '📐 Blender', callback_data='Blender')],
    [InlineKeyboardButton(text='💻 Visual Studio Code', callback_data='VScode'), InlineKeyboardButton(text = '👨‍💻 PyCharm', callback_data='PyCharm')],
])

back_to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')]
])