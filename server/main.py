from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables, delete_tables


import logging
from zoneinfo import ZoneInfo
from aiogram import Dispatcher, Bot, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.fsm.storage.redis import RedisStorage


from config import BOT_TOKEN, WEBAPP_URL
import asyncio




async def lifespan(app: FastAPI):
    
    await bot.set_webhook(url = f"{WEBAPP_URL}/webhook")
    
    
    await create_tables()
    print("База готова")








bot = Bot(BOT_TOKEN)
storage = RedisStorage.from_url("redis://localhost:6379/2")
app = FastAPI(lifespan=lifespan)


dp = Dispatcher()


async def main():
    logging.info("Бот запущен и готов к приему сообщений")

   #  await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot, allowed_updates=dp.resolve_used_update_types(), skip_updates=True
    )
builder = InlineKeyboardBuilder().button(text='ddsdsd', web_app=WebAppInfo(url=WEBAPP_URL))




@dp.message(CommandStart(), F.chat.type == 'private')
async def handle_start(message: Message):
   message.answer('привет', reply_markup=builder)






if __name__ == "__main__":
   asyncio.run(main())
