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
    fake_task_description = []  # тут зберігатимемо description задачі

    """Візьмемо 300 юзерів з faker і помістимо їх у потрібну змінну"""
    fake_data = faker.Faker()

    # Створимо набір юзерів та emails у кількості number_users
    for _ in range(number_users):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

    # Згенеруємо тепер імя та опис для задач у кількості number_tasks'''
    for _ in range(number_tasks):
        fake_task_names.append(fake_data.sentence(nb_words=5))
        fake_task_description.append(fake_data.text(max_nb_chars=100))

    # fake_status = [("new",), ("in progress",), ("completed",)]

    return fake_users, fake_emails, fake_task_names, fake_task_description


# users, emails, task_names, task_descriptions = generate_fake_data(
# NUMBER_USERS, NUMBER_TASKS
# )
# print(users)
# print(emails)
# print(task_names)
# print(task_descriptions)

statuses = [("new",), ("in progress",), ("completed",)]


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
                choice(task_names),
                choice(task_descriptions),
                choice(statuses),
                randint(1, NUMBER_USERS),
            )
        )

    for_status = []
    # для таблиці статусів
    # id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50) UNIQUE NOT NULL
    for status_name in statuses:
        for_status.append((status_name))

    return for_users, for_tasks, for_status


# users, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))

# print(users)
# print(tasks)
# print(status)


def insert_data_to_db(users, tasks, status) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними

    with sqlite3.connect("tables.db") as con:

        cur = con.cursor()

        """Заповнюємо таблицю users. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, помітимо
        знаком заповнювача (?) """

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""

        """Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипту, а другим - дані (список кортежів)."""

        cur.executemany(sql_to_users, users)

        # Далі вставляємо дані про tasks. Напишемо для нього скрипт і вкажемо змінні

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                               VALUES (?, ?, ?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_tasks, tasks)

        # Останньою заповнюємо таблицю із зарплатами

        sql_to_status = """INSERT INTO name
                              VALUES (?)"""

        # Вставляємо дані про зарплати

        cur.executemany(sql_to_status, status)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    users, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(users, tasks, status)