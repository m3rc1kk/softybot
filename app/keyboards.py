from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🖍️ Графические редакторы', callback_data='Graphic Editors'), InlineKeyboardButton(text = '💬 Мессенджеры', callback_data='Messengers')],
    [InlineKeyboardButton(text='💻 Офисные программы', callback_data='Office Programs'), InlineKeyboardButton(text = '👨‍💻 Среды для программирования', callback_data='IDE')],
])

action_with_program = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🎥 Найти видео по запросу', callback_data='find_video'), InlineKeyboardButton(text = '📁 Получить файлы', callback_data='get_file')],
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')],
])

action_with_program_video= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🎥 Найти видео по запросу', callback_data='find_video')],
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')],
])


action_with_program_file = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '📁 Получить файлы', callback_data='get_file')],
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')],
])

back_to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '◀️В главное меню', callback_data='back_to_main')]
])

