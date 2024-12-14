"""
В тебе якось складно написано і надмірні операції, насправді все набагато простіше, ось це приклад щоб розібратись
"""

import sqlite3
import random

from faker import Faker


fake = Faker("uk_UA")
conn = sqlite3.connect("tables.db")
cursor = conn.cursor()


def fill_status_table(db_path="tables.db"):
    """
    Функція щоб додати статуси

    """

    statuses = [              # це просто копіпастимо з завдання
        ("new",),
        ("in progress",),
        ("completed",)
    ]
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany("INSERT INTO status (name) VALUES (?)", statuses)
    except sqlite3.IntegrityError as e:
        print(f"Помилка унікальності: {e}")


def fill_users_table(fake: Faker, db_path="tables.db"):
    """
    Функція щоб додати користувачів  так само по суті тільки 2 значення

    """

    users = [(fake.name(), fake.email()) for _ in range(10)]
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)
    except sqlite3.IntegrityError as e:
        print(f"Помилка унікальності: {e}")


def fill_tasks_table(fake: Faker, db_path="tables.db", num_tasks=15):
    """
    Функція щоб додати задачі, тут вже складніше , зверни увагу що нам потрібно спочатку витягнути попередні дані
     бо ми не знаємо айді юзерів і статусів
    """
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Робимо секлекти це просто щоб  дізнатись що у нас в бд по айді
            cursor.execute("SELECT id FROM status")
            status_ids = [row[0] for row in cursor.fetchall()]

            cursor.execute("SELECT id FROM users")
            user_ids = [row[0] for row in cursor.fetchall()]
            if not status_ids or not user_ids:
                print("Пусті таблиці, спочатку інші функціїї треба викликати")
                return

            tasks = []
            for _ in range(num_tasks):
                title = fake.sentence(nb_words=4)
                description = fake.text(max_nb_chars=200)
                status_id = random.choice(status_ids)
                user_id = random.choice(user_ids)
                tasks.append((title, description, status_id, user_id))

            cursor.executemany("""
                   INSERT INTO tasks (title, description, status_id, user_id) 
                   VALUES (?, ?, ?, ?)
               """, tasks)
    except sqlite3.Error as e:
        print(f"Помилка SQLite: {e}")



if __name__ == "__main__":
    fill_status_table()
    fill_users_table(fake)
    fill_tasks_table(fake)