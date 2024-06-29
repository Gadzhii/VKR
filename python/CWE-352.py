from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Пример пользователя
users = {"admin": "password"}

@app.route('/')
def home():
    return '''
        <h1>Welcome</h1>
        <form action="/login" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        <form action="/transfer" method="post">
            <p><input type=text name=to_user placeholder="Recipient">
            <p><input type=text name=amount placeholder="Amount">
            <p><input type=submit value=Transfer>
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('home'))
    return 'Invalid credentials'

@app.route('/transfer', methods=['POST'])
def transfer():
    to_user = request.form['to_user']
    amount = request.form['amount']
    # Здесь должна быть логика перевода средств
    return f'Transferred {amount} to {to_user}'

if __name__ == '__main__':
    app.run(debug=True)
