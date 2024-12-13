from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_COMPANIES = 3
NUMBER_EMPLOYESS = 30
NUMBER_POST = 5


def generate_fake_data(number_companies, number_employees, number_post) -> tuple():
    fake_companies = []  # тут зберігатимемо компанії
    fake_employees = []  # тут зберігатимемо співробітників
    fake_posts = []  # тут зберігатимемо посади
    """Візьмемо три компанії з faker і помістимо їх у потрібну змінну"""
    fake_data = faker.Faker()

    # Створимо набір компаній у кількості number_companies
    for _ in range(number_companies):
        fake_companies.append(fake_data.company())

    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_employees):
        fake_employees.append(fake_data.name())

    # Та number_post набір посад
    for _ in range(number_post):
        fake_posts.append(fake_data.job())

    return fake_companies, fake_employees, fake_posts

companies, employees, posts = generate_fake_data(
    NUMBER_COMPANIES, NUMBER_EMPLOYESS, NUMBER_POST
)
print(companies)
print(employees)
print(posts)
