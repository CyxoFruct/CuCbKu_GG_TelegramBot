import sqlite3
import json

user_id = 1114626593  # <-- замени на свой Telegram ID

DB_PATH = "datebase/users.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("SELECT member_cards FROM users WHERE user_id = ?", (user_id,))
row = cursor.fetchone()
conn.close()

if row:
    member_cards = json.loads(row[0])
    print(f"Найдено карточек: {len(member_cards)}")
    print("Содержимое:", member_cards)
else:
    print("Пользователь не найден.")