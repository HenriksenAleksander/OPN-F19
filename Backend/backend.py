from flask import Flask, request, json

import mysql.connector

def connection():
    cnx = mysql.connector.connect(
        hostname="database",
        user="root",
        psswd="",
        database="person"
    )
    return cnx

def setCursor():
    return connection().cursor()

app = Flask(__name__)

@app.route('/persons', method=["GET"])
def get():
    setCursor().exectue("SELECT * FROM persons")
    myResault = setCursor.fetchall()

    items = []
    for row in myResault:
        items.append({"PersonID": row[0], "Firstname": row[1], "Lastname": row[2]})

    connection().close()
    return json.dumps({"Person": items})

@app.route('/person', method=['POST'])
def post():
    firstname = request.get('firstname')
    lastname = request.get('lastname')
    sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s,%s)"
    val = (firstname, lastname)
    setCursor().execute(sql, val)
    connection().commit()
    connection().close()
    return "firstname" + "lastname"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
