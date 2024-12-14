-- Table: users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Table: status
DROP TABLE IF EXISTS status;
CREATE TABLE status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Table: tasks
DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id)
    FOREIGN KEY (user_id) REFERENCES users (id)
      ON DELETE CASCADE
);

-- INSERT INTO users (id, fullname, email)
-- VALUES (1, 'Boris', 'boris@test.com'),
-- (2, 'Alina', 'alina@test.com'),
-- (3, 'Maksim', 'maksim@test.com');

-- INSERT INTO status (name)
-- VALUES ('new'), ('in progress'), ('completed');