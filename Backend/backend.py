from flask import Flask, request, json

import mysql.connector

app = Flask(__name__)

def connection():
    cnx = mysql.connector.connect(
        hostname="db",
        port="3306",
        user="root",
        psswd="",
        database="person"
    )
    return cnx

@app.route('/persons', method=["GET"])
def get():
    db = connection()
    cursor = db.cursor()
    cursor.exectue("SELECT * FROM persons")
    myResault = cursor.fetchall()

    items = []
    for row in myResault:
        items.append({"PersonID":row[0], "Firstname":row[1], "Lastname":row[2]})
    cursor.close()
    db.close()
    return json.dumps(items)

@app.route('/person', method=['POST'])
def post():
    db = connection()
    cursor = db.cursor()
    reguests = request.from
    firstname = reguests['firstname']
    lastname = reguests['lastname']
    sql = "INSERT INTO persons (firstname, lastname) VALUES (%s,%s)", (firstname, lastname)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return str(firstname + lastname)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
