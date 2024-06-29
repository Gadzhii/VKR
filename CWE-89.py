import sqlite3

def unsafe_query(user_input):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    
    # Уязвимый запрос
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    connection.close()
    
    return results

# Пример использования
user_input = "admin' --"
print(unsafe_query(user_input))
