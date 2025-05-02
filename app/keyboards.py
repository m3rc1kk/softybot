from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🖍️ Adobe Photoshop', callback_data='Adobe Photoshop'), InlineKeyboardButton(text = '📐 Blender', callback_data='Blender')],
    [InlineKeyboardButton(text='💻 Visual Studio Code', callback_data='VScode'), InlineKeyboardButton(text = '👨‍💻 PyCharm', callback_data='PyCharm')],
])

action_with_program = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🎥 Найти видео по запросу', callback_data='find_video'), InlineKeyboardButton(text = '📁 Получить файл', callback_data='get_file')],
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')],
])

action_with_program_video= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🎥 Найти видео по запросу', callback_data='find_video')],
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')],
])


action_with_program_file = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '📁 Получить файл', callback_data='get_file')],
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')],
])

back_to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')]
])

