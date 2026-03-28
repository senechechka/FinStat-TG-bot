from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    wait_earn = State()
    wait_disearn = State()

