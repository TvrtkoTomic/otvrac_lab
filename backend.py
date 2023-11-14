from flask import Flask, render_template
import os
import psycopg2
app = Flask(__name__)

    
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/datatable")
def datatable():
    conn = psycopg2.connect(
        host="localhost",
        port = "5434",
        database="ducani_tehnike",
        user='postgres',
        password='bazepodataka')
    cur = conn.cursor()
    cur.execute('SELECT * FROM ducani_tehnike, vlasnici WHERE ducani_tehnike.ducan_id = vlasnici.ducan_id;')
    data = cur.fetchall()
    
    return render_template('datatable.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)