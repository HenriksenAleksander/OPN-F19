from flask import Flask, request, json

import mysql.connector

def connection():
    cnx = mysql.connector.connect(
        hostname="database",
        port="3306",
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
        items.append({"Firstname": row[1], "PersonID": row[0], "Lastname": row[2]})

    connection().close()
    return json.dumps(items)

@app.route('/person', method=['POST'])
def post():
    firstname = request.from('firstname')
    lastname = request.from('lastname')
    sql = "INSERT INTO persons (FirstName, LastName) VALUES (%s,%s)", (firstname, lastname)
    setCursor().execute(sql)
    connection().commit()
    connection().close()
    return str(firstname + lastname)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
