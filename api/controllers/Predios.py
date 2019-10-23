from flask import jsonify, request
from db.db import con

class Predio():
    global cur
    cur = con.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM Predios")
        rows = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in rows:
            registro = zip(columns, row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        con.close
    
    def create(body):
        data = (body['codigo'], body['latitud'], body['longitud'], body['terreno'], body['area'], body['imagen'])
        sql = "INSERT INTO Predios(codigo, latitud, longitud, terreno, area, imagen) VALUES(%s, %s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        con.commit()
        return {'estado': "Insertado"}, 200