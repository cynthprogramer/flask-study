from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return ' <h1> olá <br> mundo </h1>'

@app.route('/aluno')
def aluno():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def form ():
    nombre = request.form['nome']
    senha =  request.form['senha']

    if senha == '123':
        return render_template('aluno.html', n = nombre)
    else:
        return 'q senha cabulosa, n tenho'
