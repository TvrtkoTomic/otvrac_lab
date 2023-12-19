from flask import Flask, render_template, jsonify, request, Response, send_file, json
import os
import psycopg2
app = Flask(__name__)


def internal_server_error(e):
    return redirect(request.referrer)

HOST ="localhost"
PORT = "5434"
DATABASE ="ducani_tehnike"
USER ='postgres'
PASSWORD ='bazepodataka'   
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/datatable")
def datatable():
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT * FROM ducani_tehnike, vlasnici WHERE ducani_tehnike.ducan_id = vlasnici.ducan_id;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('datatable.html', data=data)
    

@app.route("/api/ducani_vlasnici", methods= ['GET'])
def svi_ducani_i_vlasnici():
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT * FROM ducani_tehnike, vlasnici WHERE ducani_tehnike.ducan_id = vlasnici.ducan_id;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    json_data = jsonify(data)
    if json_data == None:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije nađen"
    return response

@app.route("/api/ducani_vlasnici/<id>", methods= ['GET'])
def specifican_ducan_i_vlasnik(id):
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT * FROM ducani_tehnike, vlasnici WHERE ducani_tehnike.ducan_id = vlasnici.ducan_id AND ducani_tehnike.ducan_id =%s',(id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    json_data = jsonify(data)
    if json_data == None:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
    return response

@app.route("/api/ducani_tehnike/", methods= ['GET'])
def ducani_tehnike():
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('SELECT * FROM ducani_tehnike')
    data = cur.fetchall()
    cur.close()
    conn.close()
    if json_data == None:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
    return response


@app.route("/api/ducani_tehnike/<id>", methods= ['DELETE'])
def izbrisi_ducan(id):
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('''DELETE FROM ducani_tehnike WHERE ducan_id =%s''',(id,))
    conn.commit()
    cur.close()
    conn.close()
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspjesan dohvat resursa"
    return response
    

@app.route("/api/ducani_tehnike/<id>", methods= ['GET'])
def specifican_ducan(id):
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM ducani_tehnike WHERE ducani_tehnike.ducan_id =%s''',(id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    json_data = jsonify(data)
    if json_data == None:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
    return response

@app.route("/api/vlasnici/", methods= ['GET'])
def svi_vlasnici():
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM vlasnici''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    json_data = jsonify(data)
    if json_data == None:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
    return response

@app.route("/api/vlasnici/<id>", methods= ['DELETE'])
def izbrisi_vlasnik(id):
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    
    cur.execute('''DELETE FROM vlasnici WHERE vlasnici.id =%s''',(id,))
    conn.commit()
    cur.close()
    conn.close()
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspjesan dohvat resursa"
    return response
    

@app.route("/api/vlasnici/<id>", methods= ['GET'])
def specifican_vlasnik(id):
    conn = psycopg2.connect(
        host = HOST,
        port = PORT,
        database = DATABASE,
        user = USER,
        password= PASSWORD)
    cur = conn.cursor()
    cur.execute('''SELECT * FROM vlasnici WHERE vlasnici.id =%s''',(id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    json_data = jsonify(data)
    if json_data == None:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
    return response

@app.route('/api/ducani_tehnike', methods= ['POST'])
def stvori_ducan():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
    cur = conn.cursor()

    podatci = request.get_json()
    ducan_id = podatci["ducan_id"]
    naziv = podatci["naziv"]
    adresa = podatci["adresa"]
    grad = podatci["grad"]
    drzava = podatci["drzava"]
    telefonski_broj = podatci["telefonski_broj"]
    email = podatci["email"]
    geolokacija = podatci["geolokacija"]
    recenzija = podatci["recenzija"]
    postanski_broj = podatci["postanski_broj"]
    cur.execute(
        '''INSERT INTO ducani_tehnike \
        (ducan_id, naziv, adresa, grad, drzava, telefonski_broj, email, geolokacija, recenzija, postanski_broj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
        (ducan_id, naziv, adresa, grad, drzava, telefonski_broj, email, geolokacija, recenzija, postanski_broj))
    conn.commit()

    #Raskid veze sa bazom
    cur.close()
    conn.close()
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspješan dohvat resursa"
    return response

    

@app.route('/api/ducani_tehnike', methods= ['PUT'])
def osvjezi_ducan():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
    cur = conn.cursor()

    podatci = request.get_json()
    ducan_id = podatci["ducan_id"]
    naziv = podatci["naziv"]
    adresa = podatci["adresa"]
    grad = podatci["grad"]
    drzava = podatci["drzava"]
    telefonski_broj = podatci["telefonski_broj"]
    email = podatci["email"]
    geolokacija = podatci["geolokacija"]
    recenzija = podatci["recenzija"]
    postanski_broj = podatci["postanski_broj"]
    cur.execute(
        '''UPDATE ducani_tehnike SET naziv = %s, adresa = %s, grad = %s, drzava = %s, telefonski_broj = %s \
        email = %s, geolokacija = %s, recenzija = %s, postanski_broj = %s WHERE ducan_id = %s''',
        (naziv, adresa, grad, drzava, telefonski_broj, email, geolokacija, recenzija, postanski_broj, ducan_id))
    conn.commit()

    #Raskid veze sa bazom
    cur.close()
    conn.close()
   
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspjesan dohvat resursa"
    return response
    
@app.route('/api/vlasnici/', methods= ['POST'])
def stvori_vlasnika():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
    cur = conn.cursor()

    podatci = request.get_json()
    id= podatci["id"]
    ime = podatci["ime"]
    prezime = podatci["prezime"]
    ducan_id = podatci["ducan_id"]
    
    cur.execute(
        '''INSERT INTO vlasnici \
        (id, ime, prezime, ducan_id) VALUES (%s, %s, %s, %s)''',
        (id, ime, prezime, ducan_id))
    conn.commit()

    #Raskid veze sa bazom
    cur.close()
    conn.close()
    
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspjesan dohvat resursa"
    return response
    
@app.route('/api/vlasnici', methods= ['PUT'])
def osvjezi_vlasnika():
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
    cur = conn.cursor()

    podatci = request.get_json()
    id= podatci["id"]
    ime = podatci["ime"]
    prezime = podatci["prezime"]
    ducan_id = podatci["ducan_id"]
    
    cur.execute(
        '''UPDATE vlasnici SET \
         ime = %s, prezime = %s, ducan_id = %s WHERE id = %s''',
        (ime, prezime, ducan_id, id))
    conn.commit()

    #Raskid veze sa bazom
    cur.close()
    conn.close()
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspješan dohvat resursa"
    return response

@app.route('/api/doc', methods= ['GET'])
def dokumentacija():
    return send_file("openapi.json", mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)