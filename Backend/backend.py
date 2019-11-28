FROM flask import Flask, requests, json

import mysql.connector

def connection():
    cnx = mysql.connector.connect(
        hostname="database",
        user="root",
        psswd="",
        database="person"
    )
    return cnx.cursor()

app = Flask(__name__)

@app.route('/persons', method=["GET"])
def get():
    connection().exectue("SELECT * FROM persons")
    myResault = cursor.fetchall()

    return myResault

@app.route('/person', method=["POST"])
def post():
    firstname = request.from.get("firstname")
    lastname = request.from.get("lastname")
    sql = "INSERT INTO persons (Firstname, Lastname) VALUES (%s,%s)"
    val = (firstname, lastname)
    connection().execute(sql, val)
    mysql.commit()

if __name__ ='__main__':
    app.run(127.0.0.1)
