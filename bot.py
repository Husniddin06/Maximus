import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, ADMIN_IDS

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher
bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
dp = Dispatcher()

# Menyu tugmalari (Rus tilida)
def get_main_menu():
    kb = [
        [KeyboardButton(text="🎵 Музыка для тренировок")],
        [KeyboardButton(text="🔥 План тренировок"), KeyboardButton(text="⭐ PRO Аккаунт")],
        [KeyboardButton(text="📊 Мой прогресс"), KeyboardButton(text="⚙️ Настройки")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        "👋 Привет! Добро пожаловать в **FitBeat** — твой личный фитнес-помощник.\n\n"
        "Здесь ты найдешь лучшую музыку для тренировок, планы занятий и сможешь отслеживать свой прогресс.\n\n"
        "Выбери нужный раздел в меню ниже! 👇"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")

@dp.message(F.text == "⭐ PRO Аккаунт")
async def pro_account(message: types.Message):
    pro_text = (
        "💎 **PRO Аккаунт**\n\n"
        "Станьте премиум-пользователем и получите:\n"
        "✅ Доступ к эксклюзивным плейлистам (100+ треков)\n"
        "✅ Индивидуальные планы тренировок\n"
        "✅ Отсутствие рекламы\n"
        "✅ Приоритетная поддержка\n\n"
        "Стоимость: **49,000 сум / месяц**"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 Купить PRO", callback_data="buy_pro")]
    ])
    await message.answer(pro_text, reply_markup=kb, parse_mode="Markdown")

@dp.message(F.text == "🎵 Музыка для тренировок")
async def music_menu(message: types.Message):
    music_text = "🎶 Выберите жанр музыки для вашей тренировки:"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Phonk", callback_data="music_phonk"), InlineKeyboardButton(text="🎸 Rock", callback_data="music_rock")],
        [InlineKeyboardButton(text="🎧 Hip-Hop", callback_data="music_hiphop"), InlineKeyboardButton(text="⚡ Electronic", callback_data="music_electro")],
        [InlineKeyboardButton(text="🧘 Relax / Yoga", callback_data="music_relax")]
    ])
    await message.answer(music_text, reply_markup=kb)

async def main():
    if not BOT_TOKEN:
        print("Xatolik: BOT_TOKEN topilmadi! .env faylini tekshiring.")
        return
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
