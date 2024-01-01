from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Olá, mundo! Esta é uma aplicação web simples em Python.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
