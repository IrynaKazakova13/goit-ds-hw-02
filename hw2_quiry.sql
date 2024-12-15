---1 Отримати всі завдання певного користувача. 
---Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT title, description, user_id
FROM tasks as t
WHERE user_id=18;

---2 Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT *
FROM tasks t 
WHERE status_id IN 
	(SELECT id
	FROM status s 
	WHERE name="new");

---3 Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус
UPDATE tasks SET status_id = 2 WHERE id = 20;

---4 Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
SELECT *
FROM users u
WHERE id NOT IN
	(SELECT user_id
	FROM tasks t);

---5 Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('added task', 'the task has been added', 2, 6);

---6 Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT *
FROM tasks t 
WHERE status_id=3;

---7 Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE FROM tasks 
WHERE id=4;

---8 Знайти користувачів з певною електронною поштою. 
---Використайте SELECT із умовою LIKE для фільтрації за електронною поштою
SELECT *
FROM users u 
WHERE email LIKE "iwalker@example.net";

---9 Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE
UPDATE users SET fullname = "Donald Trump" WHERE id = 3;

---10 Отримати кількість завдань для кожного статусу. 
---Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT COUNT(status_id) as total_tasks, status_id
FROM tasks t 
GROUP BY status_id 

---11 Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. 
---Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT t.id, t.title, t.description, u.email AS email_address
FROM tasks AS t
JOIN users AS u ON u.id = t.user_id
WHERE u.email LIKE '%@example.org'; 

---12 Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT *
FROM tasks t 
WHERE description ISNULL;

---13 Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 
---Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT u.id, u.fullname, u.email, t.title , t.description, t.status_id
FROM users u 
INNER JOIN tasks t ON t.user_id = u.id 
WHERE t.status_id = 2;

---14 Отримати користувачів та кількість їхніх завдань. 
---Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT u.id, u.fullname, u.email, COUNT(t.title ) as total_tasks
FROM users u 
LEFT JOIN tasks t ON t.user_id = u.id 
GROUP BY t.title;












