from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message
import app.keyboards as kb
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class ProgramStates(StatesGroup):
    waiting_query = State()

router = Router()

@router.message(CommandStart())
async def main(message: Message):
    await message.answer('💠Главное меню SoftyBot \n Выбери программу — помогу разобраться!', reply_markup= kb.main)


@router.callback_query(F.data.in_(['Adobe Photoshop', 'Blender', 'VScode', 'PyCharm']))
async def ask_program(callback: CallbackQuery, state: FSMContext):
    program_name = callback.data
    await callback.answer('')
    await callback.message.edit_text(f'❕Введите свой запрос по {program_name}')
    await state.set_state(ProgramStates.waiting_query)
    await state.update_data(current_program=program_name)

@router.message(ProgramStates.waiting_query)
async def handle_program(message: Message, state: FSMContext):
    data = await state.get_data()
    program = data['current_program']
    await message.answer(f'{program}')
    await state.clear()
