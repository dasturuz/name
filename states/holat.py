from aiogram.dispatcher.filters.state import State, StatesGroup

class Murojaatlar(StatesGroup):
    ism_uchun = State()
    fam_uchun = State()
    yosh_uchun = State()
    tel_uchun = State()
    manzil_uchun = State()
    murojaat_uchun = State()
    tasdqilash = State()