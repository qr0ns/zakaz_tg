from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

POSITIONS = {
    "Менеджер": {
        "instructions": [
            "1. Инструкция по работе с клиентами",
            "2. Инструкция по оформлению заказов",
            "3. Инструкция по работе с CRM"
        ],
        "test": [
            {
                "question": "Как правильно обращаться к клиенту?",
                "options": ["На ты", "По имени", "Эй, ты", "Без обращения"],
                "correct": 1
            },
            {
                "question": "Что делать при возражении клиента?",
                "options": ["Прервать разговор", "Выяснить причину", "Настаивать на своем", "Передать другому менеджеру"],
                "correct": 1
            }
        ]
    },
    "Разработчик": {
        "instructions": [
            "1. Инструкция по Git",
            "2. Инструкция по код-ревью",
            "3. Инструкция по работе с задачами"
        ],
        "test": [
            {
                "question": "Как часто нужно делать коммиты?",
                "options": ["Раз в день", "По завершению задачи", "После каждого значимого изменения", "Перед уходом домой"],
                "correct": 2
            },
            {
                "question": "Что делать перед пулл-реквестом?",
                "options": ["Проверить код", "Написать тесты", "Запустить линтер", "Все вышеперечисленное"],
                "correct": 3
            }
        ]
    }
}

keyboard_start = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=position) for position in POSITIONS.keys()]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

keyboard_ready_to_test = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Я изучил инструкции, готов к тесту")]],
        resize_keyboard=True,
        one_time_keyboard=True
    )

manager_test_1 = POSITIONS["Менеджер"]["test"][0]['question']
manager_test_2 = POSITIONS["Менеджер"]["test"][1]['question']

dev_test_1 = POSITIONS["Разработчик"]["test"][0]['question']
dev_test_2 = POSITIONS["Разработчик"]["test"][1]['question']

keyboard_test_manager_1 = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=option) for option in POSITIONS["Менеджер"]["test"][0]["options"]]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

keyboard_test_manager_2 = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=option) for option in POSITIONS["Менеджер"]["test"][1]["options"]]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

keyboard_test_dev_1 = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=option) for option in POSITIONS["Разработчик"]["test"][0]["options"]]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

keyboard_test_dev_2 = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=option) for option in POSITIONS["Разработчик"]["test"][1]["options"]]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

