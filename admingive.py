import sqlite3

users_list = [1114626593, 347632821, 462179661, 776301286]

DB_PATH = "datebase/users.db"
my_user_id = 776301286  # Твой Telegram user_id
admin_level = 100         # Уровень админа

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Проверим, есть ли уже пользователь
cur.execute("SELECT user_id FROM users WHERE user_id = ?", (my_user_id,))
if cur.fetchone() is None:
    # Добавим пользователя с админ уровнем
    cur.execute("INSERT INTO users (user_id, admin_lvl) VALUES (?, ?)", (my_user_id, admin_level))
else:
    # Обновим уровень админа
    cur.execute("UPDATE users SET admin_lvl = ? WHERE user_id = ?", (admin_level, my_user_id))

conn.commit()
conn.close()

print("Админка выдана!")