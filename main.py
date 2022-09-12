import sqlite3
import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

# ----------------------------------------------------

@app.route('/listaPreguntas', methods=['GET', 'POST'])
def listaPreguntas():
    conn = sqlite3.connect('dataBase.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""SELECT *
                        FROM Preguntas;
                    """)
    rows = cur.fetchall()
    preguntas = []
    for fila in rows:
        pregunta = {
            "id_pregunta": fila[0],
            "pregunta": fila[1],
            "categoria": fila[2],
            "nivel": fila[3]
        }
        preguntas.append(pregunta)
    return jsonify(preguntas)


@app.route('/get')
def get():
    return render_template("get.html")

# ----------------------------------------------

@app.route('/agregarPreguntas', methods=['GET','POST'])
def crear():
    conn = sqlite3.connect('dataBase.db')

    preg = request.form['textoPregunta']
    nivel = request.form['nivel']
    categ = request.form['categoria']

    q = f"""INSERT INTO Preguntas(pregunta, categoria,nivel)
          VALUES('{preg}','{categ}','{nivel}');"""
    conn.execute(q)
    conn.commit()
    conn.close()
    return 'Exito'

      
@app.route('/post')
def post():
    return render_template("post.html")

# ------------------------------------------

@app.route('/put')
def put():
    return render_template("put.html")

@app.route('/modificarPregunta', methods=['PUT'])
def modificarBase():
    preg = request.form['textoPregunta']
    id = request.form['idPregunta']
    print(preg, id)
    conn = sqlite3.connect('dataBase.db')
    cur = conn.cursor()
    cur.execute(f"""UPDATE Preguntas
      SET pregunta='{preg}'
      WHERE id_pregunta={id};""")
    conn.commit()
    conn.close()

    return 'Exito'

# -------------------------------------------------
    
@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/borrarPregunta', methods=['DELETE'])
def borrarBase():
    id = request.form['idPregunta']
    print(id)
    conn = sqlite3.connect('dataBase.db')
    conn.execute(f"""DELETE FROM Preguntas
                  WHERE id_pregunta={id};""")
    conn.commit()
    conn.close()

    return 'Exito'

    
app.run(host='0.0.0.0', port=81)
