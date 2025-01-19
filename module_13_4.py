from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = '8033982728:AAG30YO2LQoqEW2xhv2k--QrOCRnA42PJeU'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.'
                         '\nНапиши "Calories", чтобы узнать свою норму калорий.')

@dp.message_handler(text=['Calories'])
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

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введи команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)