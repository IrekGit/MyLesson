import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Заполнение таблицы 10 записями
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# Обновление баланса у каждой 2-ой записи начиная с 1-ой
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

# Удаление каждой 3-ей записи начиная с 1-ой
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# Выборка всех записей, где возраст не равен 60 и вывод результата в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
records = cursor.fetchall()
for record in records:
    print(f"Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}")

connection.commit()
connection.close()