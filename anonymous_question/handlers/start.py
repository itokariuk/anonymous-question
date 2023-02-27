from aiogram import Router
from aiogram.types import Message

from anonymous_question.services.templates import render_template


start_router = Router()


async def start(message: Message):
    await message.answer(render_template("start.j2"))
