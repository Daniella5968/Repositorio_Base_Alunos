from flask import Flask, request, jsonify, render_template, json, redirect, url_for

app = Flask(__name__)

notas = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request. method == 'GET':
        return render_template('index.html', notas=notas)
    elif request.method == 'POST':
        nota = request.form['nota']
        notas.append(nota)
        return redirect(url_for('index'))
    