from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.button import but, but2
from loader import dp, bot
from states.holat import Murojaatlar


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! \n \nUshbu bot orqali siz Oliy ta'lim, fan va innovatsiyalar vazirligi farg‘ona viloyati boshqarmasi uchun ariza yoki shikoyatingizni kiritishingiz mumkin.", reply_markup=but)


@dp.message_handler(text="Ariza kiritish ✍️")
async def bot_start(message: types.Message):
    await message.answer(text="Ismingizni kiriting:")
    await Murojaatlar.ism_uchun.set()

@dp.message_handler(state=Murojaatlar.ism_uchun)
async def bot_start(message: types.Message, state=FSMContext):
    ismi = message.text
    await state.update_data({"ism":ismi})
    await message.answer(text="Familyangizni kiriting:")
    await Murojaatlar.fam_uchun.set()

@dp.message_handler(state=Murojaatlar.fam_uchun)
async def bot_start(message: types.Message, state=FSMContext):
    fami = message.text
    await state.update_data({"fam":fami})
    await message.answer(text="Yoshingizni kiriting:")
    await Murojaatlar.yosh_uchun.set()

@dp.message_handler(state=Murojaatlar.yosh_uchun)
async def bot_start(message: types.Message, state=FSMContext):
    yoshi = message.text
    await state.update_data({"yosh":yoshi})
    await message.answer(text="Telefon raqamingizni kiriting:")
    await Murojaatlar.tel_uchun.set()

@dp.message_handler(state=Murojaatlar.tel_uchun)
async def bot_start(message: types.Message, state=FSMContext):
    teli = message.text
    await state.update_data({"tel":teli})
    await message.answer(text="Manzilingizni kiriting:")
    await Murojaatlar.manzil_uchun.set()

@dp.message_handler(state=Murojaatlar.manzil_uchun)
async def bot_start(message: types.Message, state=FSMContext):
    manzili = message.text
    await state.update_data({"manzil":manzili})
    await message.answer(text="Murojaatingiz mazmunini kiriting:")
    await Murojaatlar.murojaat_uchun.set()

@dp.message_handler(state=Murojaatlar.murojaat_uchun)
async def bot_echo(message: types.Message, state=FSMContext):
    murojaati = message.text
    await state.update_data({"murojaat":murojaati})

    info = await state.get_data()

    name = info.get("ism")
    last_name = info.get("fam")
    old = info.get("yosh")
    phone = info.get("tel")
    locat = info.get("manzil")
    text = info.get("murojaat")

    send = f"Ismingiz: {name}; \n" \
           f"Familyangiz: {last_name}; \n" \
           f"Yoshingiz: {old}; \n" \
           f"Telefon raqamingiz: {phone}; \n" \
           f"Manzilingiz: {locat}; \n" \
           f"Murojaatingiz mazmuni: {text}; \n"

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=send, reply_markup=but2)
    await Murojaatlar.tasdqilash.set()

@dp.message_handler(state=Murojaatlar.tasdqilash, text="Tasdiqlash 👌")
async def bot_echo(message: types.Message, state=FSMContext):

    info = await state.get_data()

    name = info.get("ism")
    last_name = info.get("fam")
    old = info.get("yosh")
    phone = info.get("tel")
    locat = info.get("manzil")
    text = info.get("murojaat")

    send = f"Ismingiz: {name}; \n" \
           f"Familyangiz: {last_name}; \n" \
           f"Yoshingiz: {old}; \n" \
           f"Telefon raqamingiz: {phone}; \n" \
           f"Manzilingiz: {locat}; \n" \
           f"Murojaatingiz mazmuni: {text}; \n"

    user_id = message.from_user.id
    await bot.send_message(chat_id='@jghyrt', text=send)
    await bot.send_message(chat_id=user_id, text="Ariza yuborildi")
    await state.finish()
