from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
import app.keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import aiohttp


class ProgramStates(StatesGroup):
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


@router.callback_query(F.data.in_(['Adobe Photoshop', 'Blender', 'VScode', 'PyCharm']))
async def ask_program(callback: CallbackQuery, state: FSMContext):
    program_name = callback.data
    await callback.answer('')
    await callback.message.edit_text(f'💡Введите свой запрос по {program_name}')
    await state.set_state(ProgramStates.waiting_query)
    await state.update_data(current_program=program_name)

@router.message(ProgramStates.waiting_query)
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
