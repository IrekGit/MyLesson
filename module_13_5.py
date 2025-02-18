from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = 'Номер токена'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton('Рассчитать'))
    keyboard.add(types.KeyboardButton('Информация'))

    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью.\n'
        'Выбери действие через нажатие на кнопки, расположенные в нижней части экрана.\n'
        'Кнопка "Рассчитать" - некий расчет согласно информации по кнопке "Информация";)',
        reply_markup=keyboard
    )

@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введи свой возраст (сколько тебе полных лет):')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    age = int(message.text)
    await state.update_data(age=age)
    await message.answer('Введи свой рост (в см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    growth = int(message.text)
    await state.update_data(growth=growth)
    await message.answer('Введи свой вес (в кг):')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    weight = int(message.text)
    await state.update_data(weight=weight)
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Твоя норма: {calories:.2f} ккал в день.')
    await state.finish()

@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('Я помогу рассчитать твою норму калорий.\n'
                         'Нажми "Рассчитать", чтобы начать.')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введи команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)