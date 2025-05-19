import os

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message, FSInputFile, BufferedInputFile
import app.keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import aiohttp


PROGRAM_FOLDER = 'program_files'
PROGRAM_FILES = {
    'IDE': ['Pycharm.pdf', ],
    'Office Programs': ['Word.pdf', ],
    'Messengers': ['VK_Android.pdf', 'VK_IOS.pdf', 'VK_Web.pdf', 'VK_PC.pdf', 'WhatsApp_Android.pdf', 'WhatsApp_IOS.pdf', ],
    'Graphic Editors': ['Pycharm.pdf', ],
}

class ProgramActions(StatesGroup):
    waiting_action = State()
    waiting_query = State()

router = Router()


async def search_rutube_video(query: str, program_name: str):
    search_query = f"{program_name} {query}"
    url = "https://rutube.ru/api/search/video/"
    params = {
        "query": search_query,
        "format": "json",
        "no_adult": "1",
        "sort": "views",
        "page": "1",
        "limit": "1"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if data.get('results'):
                    video_id = data['results'][0]['id']
                    return f"https://rutube.ru/video/{video_id}/"
    return None


@router.message(CommandStart())
async def main(message: Message):
    await message.answer('💠Главное меню SoftyBot \n Выбери программу — помогу разобраться!', reply_markup= kb.main)

@router.callback_query(F.data.in_(['IDE', 'Office Programs', 'Messengers', 'Graphic Editors']))
async def select_program(callback: CallbackQuery, state:FSMContext):
    program_name = callback.data
    await callback.answer()
    await state.update_data(current_program=program_name)

    await callback.message.edit_text(f'🔹 Вы выбрали: {program_name}\n Выберите действие', reply_markup=kb.action_with_program)

    await state.set_state(ProgramActions.waiting_action)

@router.callback_query(ProgramActions.waiting_action, F.data == 'find_video')
async def ask_program(callback:CallbackQuery , state: FSMContext):
    data = await state.get_data()
    program_name = data['current_program']
    try:
        await callback.message.edit_text(f'💡Введите свой запрос по {program_name}')
    except:
        await callback.message.answer(f'💡Введите свой запрос по {program_name}')
    await state.set_state(ProgramActions.waiting_query)
    await callback.answer()


from aiogram.types import InputMediaDocument


@router.callback_query(ProgramActions.waiting_action, F.data == 'get_file')
async def send_useful_file(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    program_name = data['current_program']

    file_names = PROGRAM_FILES.get(program_name)
    if file_names:
        media_group = []
        files_available = False
        await callback.message.answer(f'🧿 Полезные файлы для {program_name}')
        for file_name in file_names:
            file_path = os.path.join(PROGRAM_FOLDER, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    file_data = f.read()

                media_group.append(
                    InputMediaDocument(
                        media=BufferedInputFile(file_data, filename=file_name),
                    )
                )
                files_available = True

        if files_available:
            await callback.message.answer_media_group(media_group)
            await callback.message.answer(
                "Выберите следующее действие:",
                reply_markup=kb.action_with_program_video
            )
        else:
            await callback.answer("❌ Все файлы временно недоступны", show_alert=True)
    else:
        await callback.answer("ℹ️ Для этой программы нет файлов", show_alert=True)

    await state.set_state(ProgramActions.waiting_action)

@router.message(ProgramActions.waiting_query)
async def handle_program(message: Message, state: FSMContext):
    await message.answer('🔎 Мы обрабатываем ваш запрос, это может занять некоторое время')
    data = await state.get_data()
    program = data['current_program']
    user_query = message.text

    video_url = await search_rutube_video(user_query, program)

    if video_url:
        await message.answer(f"🎥 Видео по вашему запросу: \n 🔗 {video_url}")
    else:
        await message.answer("😕 Не удалось найти видео по вашему запросу")

    await message.answer('🏠Вернуться в главное меню', reply_markup=kb.back_to_main)



@router.callback_query(F.data == 'back_to_main')
async def back_to_main(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.answer('💠Главное меню SoftyBot \n Выбери программу — помогу разобраться!', reply_markup=kb.main)
