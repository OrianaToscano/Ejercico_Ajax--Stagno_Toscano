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

@app.route('/listaRespuestas', methods=['GET'])
def listaRespuestas():
    conn = sqlite3.connect('dataBase.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""SELECT *
                        FROM Respuestas
                        WHERE es_correcta=0;
                    """)
    rows = cur.fetchall()
    respuestas = []
    for fila in rows:
        respuesta = {
            "id_respuesta": fila[0],
            "es_correcta": fila[1],
            "respuesta": fila[2],
            "id_pregunta": fila[3]
        }
        respuestas.append(respuesta)
    return respuestas

@app.route('/agregarPreguntas', methods=['POST'])
def crear():
    conn = sqlite3.connect('dataBase.db')

    preg = request.form['textoPregunta']
    nivel = request.form['nivel']
    categ = request.form['categoria']

    q = f"""INSERT INTO Preguntas(pregunta, categoria,nivel)
          VALUES('{preg}','{categ}','{nivel}');"""

    try:
        conn.execute(q)
        conn.commit()
        conn.close()
        return "True"
    except:
        return 'False'
    

      
@app.route('/post')
def post():
    return render_template("post.html")

# ------------------------------------------

@app.route('/put')
def put():
    return render_template("put.html")

@app.route('/modificarRespuesta', methods=['PUT'])
def modificarBase():
    resp = request.form['textoRespuesta']
    id = request.form['idRespuesta']
    conn = sqlite3.connect('dataBase.db')
    cur = conn.cursor()
    q = f"""UPDATE Respuestas
      SET respuesta='{resp}'
      WHERE id_respuesta={id};"""

    try:
        cur.execute(q)
        conn.commit()
        conn.close()
        return ["True", f"""La modificacion ingresada a la base de datos es: '{resp}'"""]
    except:
        return "False"

# -------------------------------------------------
    
@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/borrarPregunta', methods=['DELETE'])
def borrarBase():
    id = request.form['idPregunta']
    print(id)
    conn = sqlite3.connect('dataBase.db')
    cur = conn.cursor()
    cur.execute(f"""SELECT pregunta
                        FROM Preguntas
                        WHERE id_pregunta={id};
                    """)
    data = cur.fetchall()
    conn.commit()

    q = f"""DELETE FROM Preguntas
                  WHERE id_pregunta={id};"""

    try:
        conn.execute(q)
        conn.commit()
        conn.close()
        return ["True", f"""La pregunta borrada es: '{data[0][0]}'"""]
    except:
        return "False"

    
app.run(host='0.0.0.0', port=81)
