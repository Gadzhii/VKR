import sqlite3

def safe_query(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Эта строка безопасна, так как используется параметризированный запрос
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    return cursor.fetchall()

# Вызываем функцию с безопасным параметром
result = safe_query(1)
print(result)
