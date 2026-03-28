from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.states import Form
import config
from handlers import settings

router = Router()

@router.callback_query(F.data == 'earn')
async def earn_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Введите суму зароботка: ')
    await state.set_state(Form.wait_earn)
    await callback.answer()

@router.message(StateFilter(Form.wait_earn))
async def add_earn(message: types.Message, state: FSMContext):
    count = message.text
    config.earn(count)
    kb = settings.menu_button_builder()
    await message.reply(f'Добавлена транзакция +{count}', reply_markup = kb)
    await state.clear()

@router.callback_query(F.data == 'disearn')
async def disearn_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Введите суму затрат: ')
    await state.set_state(Form.wait_disearn)
    await callback.answer()

@router.message(StateFilter(Form.wait_disearn))
async def add_disearn(message: types.Message, state: FSMContext):
    count = message.text
    config.disearn(count)
    kb = settings.menu_button_builder()
    await message.reply(f'Добавлена транзакция -{count}', reply_markup = kb)
    await state.clear()

@router.callback_query(F.data == 'stats')
async def stats_handler(callback: CallbackQuery):
    kb = settings.menu_button_builder()
    await callback.message.edit_text('СТАТИСТИКА ТРАНЗАКЦИЙ \n' \
    f'Всего заработано {config.stats["total"]}\n' \
    f'Затрат {config.stats["disearn"]}\n' \
    f'Заработано чистыми {config.stats["earn"]}',
    reply_markup = kb
    )
    await callback.answer()


