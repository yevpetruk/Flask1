"""
Ошибка в декораторе, в строке @app.route(") пропущена закрывающая
кавычка и не указан сам маршрут

Исправленный код:
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

"""