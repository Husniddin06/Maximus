import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, ADMIN_IDS

# Logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
dp = Dispatcher()

# --- KEYBOARDS ---
def get_main_menu():
    kb = [
        [KeyboardButton(text="💪 START WORKOUT")],
        [KeyboardButton(text="📊 PROGRESS"), KeyboardButton(text="🍗 NUTRITION")],
        [KeyboardButton(text="🎧 MUSIC"), KeyboardButton(text="💎 PRO")],
        [KeyboardButton(text="⚙️ SETTINGS")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_workout_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ DONE", callback_data="workout_done"), 
         InlineKeyboardButton(text="❌ SKIP", callback_data="workout_skip")]
    ])
    return kb

def get_music_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔥 HARD", callback_data="music_hard")],
        [InlineKeyboardButton(text="😌 CHILL", callback_data="music_chill")],
        [InlineKeyboardButton(text="🧠 FOCUS", callback_data="music_focus")]
    ])
    return kb

# --- HANDLERS ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Bu yerda bazaga foydalanuvchini qo'shish logikasi bo'ladi
    welcome_text = (
        "👋 **Привет, Атлет!**\n\n"
        "Добро пожаловать в твой личный фитнес-центр в Telegram.\n"
        "Готов стать лучше сегодня?\n\n"
        "🏆 **Твой уровень:** Beginner\n"
        "✨ **XP:** 0\n\n"
        "Выбери действие в меню ниже! 👇"
    )
    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="Markdown")

@dp.message(F.text == "💪 START WORKOUT")
async def start_workout(message: types.Message):
    workout_text = (
        "🏋️ **Сегодняшняя тренировка:**\n"
        "Грудь + Трицепс\n\n"
        "1. Жим лежа (Bench Press) - 3x12\n"
        "2. Отжимания (Push ups) - 3x15\n"
        "3. Брусья (Dips) - 3x10\n\n"
        "Нажми DONE, когда закончишь! 🔥"
    )
    await message.answer(workout_text, reply_markup=get_workout_kb(), parse_mode="Markdown")

@dp.callback_query(F.data == "workout_done")
async def workout_done(callback: types.CallbackQuery):
    # XP qo'shish logikasi
    await callback.answer("Отлично! +10 XP 🔥")
    await callback.message.edit_text("✅ Тренировка завершена! Ты стал сильнее.\n\n🏆 **+10 XP** добавлено в твой профиль.")

@dp.message(F.text == "🎧 MUSIC")
async def music_menu(message: types.Message):
    await message.answer("🎶 Выберите ритм для тренировки:", reply_markup=get_music_kb())

@dp.message(F.text == "🍗 NUTRITION")
async def nutrition_menu(message: types.Message):
    nutrition_text = (
        "🥗 **Твой план питания:**\n\n"
        "🍳 **Завтрак:** Яйца + Хлеб\n"
        "🍚 **Обед:** Рис + Мясо\n"
        "🥛 **Ужин:** Творог\n\n"
        "💡 *Обновитесь до PRO для детального подсчета калорий!*"
    )
    await message.answer(nutrition_text, parse_mode="Markdown")

@dp.message(F.text == "💎 PRO")
async def pro_menu(message: types.Message):
    pro_text = (
        "💎 **PRO СИСТЕМА**\n\n"
        "**FREE:**\n"
        "• Обычные тренировки\n"
        "• Базовый план питания\n\n"
        "**PRO:**\n"
        "• Персональный план\n"
        "• PDF отчеты\n"
        "• AI консультации\n"
        "• Эксклюзивная музыка\n\n"
        "💳 Оплата через Telegram Stars ⭐ или SBP"
    )
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Купить PRO ⭐", callback_data="buy_stars")],
        [InlineKeyboardButton(text="Оплата через SBP 💳", callback_data="buy_sbp")]
    ])
    await message.answer(pro_text, reply_markup=kb, parse_mode="Markdown")

@dp.message(F.text == "📊 PROGRESS")
async def progress_menu(message: types.Message):
    progress_text = (
        "📊 **Твой прогресс:**\n\n"
        "🏆 Уровень: **Beginner**\n"
        "🔥 Всего XP: **0**\n"
        "📅 Тренировок на этой неделе: **0**\n\n"
        "Продолжай в том же духе! 💪"
    )
    await message.answer(progress_text, parse_mode="Markdown")

async def main():
    if not BOT_TOKEN:
        print("Xatolik: BOT_TOKEN topilmadi!")
        return
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
