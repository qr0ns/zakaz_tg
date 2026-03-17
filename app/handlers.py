import aiosqlite
from aiosqlite import cursor

from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import keyboard_start, POSITIONS, keyboard_test_manager_1,keyboard_test_manager_2, keyboard_ready_to_test

from keyboards import manager_test_1, manager_test_2, dev_test_1, dev_test_2
from keyboards import keyboard_test_dev_1, keyboard_test_dev_2

router = Router()

answers = {}

position = ''

print(answers)

class Form(StatesGroup):
    fio = State()
    
    position = State()
    
    study_manager = State()
    study_dev = State()
    
    testing = State()
    
    question_manager = State()
    question_dev = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(f'Добро пожаловать! Для начала работы введите ваше ФИО:')
    await state.set_state(Form.fio)
    
    
@router.message(Form.fio)
async def process_fio(message: Message, state: FSMContext):
    answers[message.from_user.id] = [message.text]
    print(answers)
    await message.answer("Выберите вашу должность:", reply_markup=keyboard_start)
    await state.set_state(Form.position)
    
    
@router.message(Form.position)
async def process_position(message: Message, state: FSMContext):
    global position
    position = message.text
    if position not in POSITIONS:
        await message.answer("Пожалуйста, выберите должность из предложенных вариантов.")
        return
    answers[message.from_user.id].append(position)
    instructions = POSITIONS[position]["instructions"]
    instructions_text = "Пожалуйста, изучите следующие инструкции:\n\n" + "\n\n".join(instructions)
    
    
    await message.answer(instructions_text, reply_markup=keyboard_ready_to_test)
    await state.set_state(Form.study_manager if position == "Менеджер" else Form.study_dev)
    
print(answers)

# !!!  Manger handlers  !!!

@router.message(Form.study_manager, F.text == "Я изучил инструкции, готов к тесту")
async def process_study(message: Message, state: FSMContext):
    await message.answer(f"Начинаем тест! \n\n" + f'❗Первый вопрос❗\n\n {manager_test_1}', reply_markup=keyboard_test_manager_1)
    await state.set_state(Form.question_manager)    
    

@router.message(Form.question_manager)
async def process_question_1(message: Message, state: FSMContext):
    answers[message.from_user.id].append(message.text)
    await message.answer(f"Ответ принят, следующий вопрос:\n\n {manager_test_2}", reply_markup=keyboard_test_manager_2)
    await state.set_state(Form.testing)


# !!!  Dev test  !!!
    
@router.message(Form.study_dev, F.text == "Я изучил инструкции, готов к тесту")
async def process_study(message: Message, state: FSMContext):
    await message.answer(f"Начинаем тест! \n\n" + f'❗Первый вопрос❗\n\n {dev_test_1}', reply_markup=keyboard_test_dev_1)
    await state.set_state(Form.question_dev)
    

@router.message(Form.question_dev)
async def process_question_1(message: Message, state: FSMContext):
    answers[message.from_user.id].append(message.text)
    await message.answer(f"Ответ принят, следующий вопрос:\n\n {dev_test_2}", reply_markup=keyboard_test_dev_2)
    await state.set_state(Form.testing)

print(answers)

# !!!  Проверка на прохождение теста  !!!

@router.message(Form.testing)
async def process_question_2(message: Message, state: FSMContext, bot: Bot):
    answers[message.from_user.id].append(message.text)
    answers[message.from_user.id].append({})
    print(answers)
    answers[message.from_user.id][4].setdefault('score', 0)
    if answers[message.from_user.id][2] == POSITIONS[position]['test'][0]['options'][POSITIONS[position]['test'][0]['correct']]:
        answers[message.from_user.id][4]['score'] += 1
        print(answers)
        
    if answers[message.from_user.id][3] == POSITIONS[position]['test'][1]['options'][POSITIONS[position]['test'][1]['correct']]:
        answers[message.from_user.id][4]['score'] += 1
        print(answers)
        
    if answers[message.from_user.id][4]['score'] == 2:
        await message.answer(f"{message.from_user.username}, вы прошли тест! Поздравляем!")
        await bot.send_message(chat_id=980105774, text=f'Здравствуйте, @{message.from_user.username} прошел ваш тест на позицию {position}.')
    else:
        await message.answer("Вы не прошли тест! Попробуйте еще раз!")
    print(answers)
    await state.clear()
    
