from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Получаем параметр 'name' из запроса
    name = request.args.get('name', '')
    # Вставляем параметр 'name' напрямую в HTML без экранирования
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
