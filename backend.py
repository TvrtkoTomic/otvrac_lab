from flask import Flask, render_template, jsonify, request, Response, send_file, json, url_for, session,redirect
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
import psycopg2
from functools import wraps

ENV_FILE = find_dotenv('app.env')
if ENV_FILE:
    load_dotenv(ENV_FILE)
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
print(app.secret_key)
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

def internal_server_error(e):
    return redirect(request.referrer)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('user') is None:
            return redirect(url_for('login'))
        try:
            return f(*args, **kwargs)
        except OAuthError:
            return redirect(url_for('logout'))

    return decorated

HOST ="localhost"
PORT = "5434"
DATABASE ="ducani_tehnike"
USER ='postgres'
PASSWORD ='bazepodataka'   
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/info")
@requires_auth
def info():
    return render_template('info.html', session=session.get('user'))


@app.route("/datatable")
@requires_auth
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

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )
@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/home")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/home")
@requires_auth
def home():
    return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

    

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
    context = {
        "@context": {
            "vlasnici": "https://schema.org/Person",
            "email": "https://schema.org/email",
            "location": "https://schema.org/GeoCoordinates"
        }
    }
    
    json_data = json.dumps(data)
    context = json.dumps(context) 
    json_data = context + json_data
    if json_data != "":
        response = app.response_class(response=json_data,
                                  status=200,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data,
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
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
    context = {
        "@context": {
            "vlasnici": "https://schema.org/Person",
            "email": "https://schema.org/email",
            "location": "https://schema.org/GeoCoordinates"
        }
    }
    
    json_data = json.dumps(data)
    context = json.dumps(context) 
    json_data = context + json_data
    if json_data != "":
        response = app.response_class(response=json_data,
                                  status=200,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data,
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
    context = {
        "@context": {
            "email": "https://schema.org/email",
            "location": "https://schema.org/GeoCoordinates"
        }
    }
    
    json_data = json.dumps(data)
    context = json.dumps(context) 
    json_data = context + json_data
    if json_data != "":
        response = app.response_class(response=json_data.get_data(as_text=True),
                                  status=200,
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
    context = {
        "@context": {
            "vlasnici": "https://schema.org/Person",
            "email": "https://schema.org/email",
            "location": "https://schema.org/GeoCoordinates"
        }
    }
    
    json_data = json.dumps(data)
    context = json.dumps(context) 
    json_data = context + json_data
    if json_data != "":
        response = app.response_class(response=json_data,
                                  status=200,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data,
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
    context = {
        "@context": {
            "ime": "https://schema.org/givenName",
            "prezime": "https://schema.org/familyName",
        }
    }
    
    json_data = json.dumps(data)
    context = json.dumps(context) 
    json_data = context + json_data
    if json_data != "":
        response = app.response_class(response=json_data,
                                  status=200,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data,
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
    context = {
        "@context": {
            "@context": {
            "ime": "https://schema.org/givenName",
            "prezime": "https://schema.org/familyName",
        }
        }
    }
    
    json_data = json.dumps(data)
    context = json.dumps(context) 
    json_data = context + json_data
    if json_data != "":
        response = app.response_class(response=json_data,
                                  status=200,
                                  mimetype='application/json')
        response.headers['Message'] = "Uspjesan dohvat resursa"
    else:
        response = app.response_class(response=json_data,
                                  status=404,
                                  mimetype='application/json')
        response.headers['Message'] = "Resurs nije naden"
    return response

@app.route('/api/ducani_tehnike', methods= ['POST'])
def stvori_ducan():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
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
    response.headers['Message'] = "Uspjesan dohvat resursa"
    return response

    

@app.route('/api/ducani_tehnike', methods= ['PUT'])
def osvjezi_ducan():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
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
        '''UPDATE ducani_tehnike SET naziv = %s, adresa = %s, grad = %s, drzava = %s, telefonski_broj = %s, email = %s, geolokacija = %s, recenzija = %s, postanski_broj = %s WHERE ducan_id = %s''',
        (naziv, adresa, grad, drzava, telefonski_broj, email, geolokacija, recenzija, postanski_broj, ducan_id))
    conn.commit()

    #Raskid veze sa bazom
    cur.close()
    conn.close()
   
    response = app.response_class(
                                  status=200,
                                  mimetype='application/json')
    response.headers['Message'] = "Uspjesno azuriranje resursa"
    return response
    
@app.route('/api/vlasnici/', methods= ['POST'])
def stvori_vlasnika():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
        database=DATABASE,
        user=USER,
        password=PASSWORD)
    cur = conn.cursor()

    podatci = request.get_json(force=True)
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
    response.headers['Message'] = "Uspjesno stvaranje resursa"
    return response
    
@app.route('/api/vlasnici', methods= ['PUT'])
def osvjezi_vlasnika():
    conn = psycopg2.connect(
        host=HOST,
        port=PORT,
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
    response.headers['Message'] = "Uspjesno azuriranje resursa"
    return response

@app.route('/api/doc', methods= ['GET'])
def dokumentacija():
    return send_file("openapi.json", mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)