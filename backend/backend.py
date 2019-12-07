from flask import Flask, render_template, request ,jsonify, json
import mysql.connector
app = Flask(__name__)


#connection to db
def connectDB():
        mydb= mysql.connector.connect(
        host="db",
        port="3306",
        user="root",
        passwd="",
        database="personDB"
        )
        return mydb
        


@app.route('/person', methods=['POST'])
def Post():
        db = connectDB()
        details = request.form
        firstname = details['firstname']
        lastname = details['lastname']
        cursor = db.cursor()
        cursor.execute("INSERT INTO persons(Firstname, Lastname) VALUES (%s, %s)", (firstname, lastname))
        db.commit()
        cursor.close()
        db.close()
        
        
        retJson = {
                "firstname":firstname,
                "lastname":lastname
        }
        
        
        return jsonify(retJson)

@app.route('/persons', methods=['GET'])
def Get():
        db = connectDB()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM persons")
        dbResult = cursor.fetchall()
        data= []
        for row in dbResult:
                data.append({'PersonID':row[0], 'Firstname': row[1], 'Lastname':row[2]})
        cursor.close()
        db.close()
        
        return json.dumps(data)



if __name__ == '__main__':
        app.run(host="0.0.0.0",debug=True)