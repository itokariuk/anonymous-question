from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from anonymous_question.services.templates import render_template


start_router = Router()


@start_router.message(CommandStart)
async def start(message: Message):
    await message.answer(render_template("start.j2"))
