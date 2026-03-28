from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text = 'Главное меню', callback_data = 'main_menu')]
    ])

    await message.answer("Привет, ты попал в бота для улучшеного ведения финансовой статистики \n" \
    "Нажми на кнопку Главное меню, и начни вести свой путь", reply_markup = kb)

def menu_button_builder():
    kb = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text = 'Главное меню', callback_data = 'main_menu')]
    ])
    return kb

def main_menu_builder():
    kb = InlineKeyboardMarkup(inline_keyboard = [
        [InlineKeyboardButton(text = 'Добавить', callback_data = 'earn')],
        [InlineKeyboardButton(text = 'Отнять', callback_data = 'disearn')],
        [InlineKeyboardButton(text = 'Статистика', callback_data = 'stats')]
    ])
    text = (
        "ГЛАВНОЕ МЕНЮ \n" \
        "Тут вы можете зафиксировать свою прибыль, убытки, и получить статистику своего зароботка"
    )
    return text, kb

@router.callback_query(F.data == 'main_menu')
async def menu_buttonHandler(callback: CallbackQuery):
    text, kb = main_menu_builder()
    await callback.message.edit_text(
        text, reply_markup = kb
    )
    await callback.answer()

@router.message(Command('menu'))
async def menu_commHandler(message: types.Message):
    text, kb = main_menu_builder()
    await message.answer(
        text, reply_markup = kb
    )

