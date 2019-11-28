FROM flask import Flask, request

import mysql.connector

def connection():
    mysql.connector.connect(
        hostname="database",
        user="root",
        psswd="",
        database="person"
    )
    return mysql.cursor()

app = Flask(__name__)

@app.route('/persons', method=["GET"])
def get():
    connection()
    cursor.exectue("SELECT * FROM persons")
    myResault = cursor.fetchall()
    return myResault

@app.route('/person', method=["POST"])
def post():
    connection();
    firstname = request.from.get("firstname")
    lastname = request.from.get("lastname")
    sql = "INSERT INTO persons ("Firstname", "Lastname") VALUES (%s,%s)"
    val = (firstname, lastname)
    cursor.execute(sql, val)
    mysql.commit()
