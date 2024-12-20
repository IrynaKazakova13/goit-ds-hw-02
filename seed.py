from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 500
NUMBER_TASKS = 50
NUMBER_STATUS = 3


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []  # тут зберігатимемо юзерів
    fake_emails = []  # тут зберігатимемо emails
    fake_task_names = []  # тут зберігатимемо name задачі
    fake_task_description = []  # тут зберігатимемо description задачі

    fake_data = faker.Faker()

    # Створимо набір юзерів та emails у кількості number_users
    for _ in range(number_users):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

    # Згенеруємо тепер імя та опис для задач у кількості number_tasks'''
    for _ in range(number_tasks):
        fake_task_names.append(fake_data.sentence(nb_words=5))
        fake_task_description.append(fake_data.text(max_nb_chars=100))

    return fake_users, fake_emails, fake_task_names, fake_task_description


# users, emails, task_names, task_descriptions = generate_fake_data(
# NUMBER_USERS, NUMBER_TASKS
# )


def prepare_data(users, emails, task_names, task_descriptions) -> tuple():
    for_users = [] # готуємо список кортежів - імен юзерів
    fake_data = faker.Faker()
    for user in users:
        for_users.append((user, fake_data.email()))

    for_tasks = [] # для таблиці задач
    for task in task_names:
        for_tasks.append(
            (
                fake_data.sentence(nb_words=5),
                fake_data.text(max_nb_chars=100),
                randint(1, NUMBER_STATUS),
                randint(1, NUMBER_USERS),
            )
        )

    for_status = [  # для таблиці статусів
        ("new",),
        ("in progress",),
        ("completed",),
    ]
    return for_users, for_tasks, for_status

# users, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))

def insert_data_to_db(users, tasks, status) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними
    with sqlite3.connect("tables.db") as con:

        cur = con.cursor()

        # Заповнюємо таблицю users.

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (?, ?)"""

        # Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст скрипту, а другим - дані (список кортежів).

        cur.executemany(sql_to_users, users)

        # Далі вставляємо дані про tasks.

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                               VALUES (?, ?, ?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_tasks, tasks)

        # Останньою заповнюємо таблицю із статусами

        sql_to_status = """INSERT INTO status(name)
                              VALUES (?)"""

        # Вставляємо дані про статус

        cur.executemany(sql_to_status, status)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    users, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_TASKS))
    insert_data_to_db(users, tasks, status)
