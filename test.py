from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 10
NUMBER_TASKS = 5
NUMBER_STATUS = 3


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []  # тут зберігатимемо юзерів
    fake_emails = []  # тут зберігатимемо emails
    fake_task_names = []  # тут зберігатимемо name задачі
    fake_task_descriptions = []  # тут зберігатимемо description задачі

    """Візьмемо 300 юзерів з faker і помістимо їх у потрібну змінну"""
    fake_data = faker.Faker()

    # Створимо набір юзерів та emails у кількості number_users
    for _ in range(number_users):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

    # Згенеруємо тепер імя та опис для задач у кількості number_tasks'''
    for _ in range(number_tasks):
        fake_task_names.append(fake_data.sentence(nb_words=5))
        fake_task_descriptions.append(fake_data.text(max_nb_chars=100))

    # fake_status = [("new",), ("in progress",), ("completed",)]

    return fake_users, fake_emails, fake_task_names, fake_task_descriptions


# users, emails, task_names, task_descriptions = generate_fake_data(
# NUMBER_USERS, NUMBER_TASKS
# )
# print(users)
# print(emails)
# print(task_names)
# print(task_descriptions)

statuses = ["new", "in progress", "completed"]


def prepare_data(users, emails, task_names, task_descriptions) -> tuple():
    for_users = []
    # готуємо список кортежів - імен юзерів
    # id INTEGER PRIMARY KEY AUTOINCREMENT, fullname VARCHAR(100), email VARCHAR(100) UNIQUE NOT NULL
    fake_data = faker.Faker()
    for user in users:
        for_users.append((user, fake_data.email()))

    for_tasks = []
    # для таблиці задач
    # id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(100), description TEXT, status_id INTEGER, user_id INTEGER
    for task in task_names:
        for_tasks.append(
            (
                fake_data.sentence(nb_words=5),
                fake_data.text(max_nb_chars=100),
                # choice(task_names),
                # choice(task_descriptions),
                randint(1, NUMBER_USERS),
                randint(1, NUMBER_STATUS),
            )
        )

    for_status = []
    # для таблиці статусів
    # id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) UNIQUE NOT NULL
    for status_name in statuses:
        for_status.append((status_name))

    return for_users, for_tasks, for_status


users, tasks, status = prepare_data(
    *generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
)

print(users)
print(tasks)
print(status)
