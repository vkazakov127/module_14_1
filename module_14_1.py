# -*- coding: utf-8 -*-
# module_14_1.py
import sqlite3

conn = sqlite3.connect("not_telegram.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполняем Базу Данных, 10 строк
for i in range(10):
    c.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
              (f"User{i + 1}", f"example{i + 1}@gmail.com", f"{10*(i + 1)}", "1000"))
# Записываем изменения
conn.commit()

# Обновить поле "balance" у каждой второй записи, начиная с первой, на 500
c.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2")
# Записываем изменения
conn.commit()

# Удалить каждую 3ую запись в таблице начиная с 1ой
c.execute("DELETE FROM Users WHERE not ((id - 1) % 3)")
# Записываем изменения
conn.commit()

# Сделать выборку всех записей при помощи fetchall(), где возраст не равен 60
# и вывести их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
c.execute("SELECT username, email, age, balance FROM Users WHERE age <> 60")
users = c.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")
# Закрываем соединение
conn.close()

# ------------- The End -------------
