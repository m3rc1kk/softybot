from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

router = Router()

@router.message(CommandStart())
async def main(message: Message):
    await message.answer('💠 Главное меню SoftyBot \n Выбери программу — помогу разобраться!')