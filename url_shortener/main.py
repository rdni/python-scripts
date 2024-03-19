import time
from flask import Flask, redirect, abort, request
import sqlite3
from os import getcwd
from os.path import join
import base64
import urllib
from utils import *

app = Flask(__name__)
database = sqlite3.connect(join(getcwd(), "database.db"))

database.execute(
    "CREATE TABLE IF NOT EXISTS urls(short_url, long_url, timestamp)"
)
database.commit()
database.close()

@app.route("/<name>", methods = ["GET"])
def get_url(name):
    if not safe(name):
        abort(404)
    
    database = sqlite3.connect(join(getcwd(), "database.db"))
    cur = database.cursor()
    cur.execute(f"SELECT * FROM urls WHERE short_url='{name}'")
    
    result = cur.fetchone()
    
    database.close()
    
    if result is None:
        abort(404)
        
    print(result[1])
    
    return redirect(str(base64.b64decode(result[1]).decode("utf-8"))[2:-1], code=301)

@app.route("/create", methods = ["POST"])
def create_url():
    url = request.values.get("url")
    
    if not isurl(url):
        abort(400)
    
    encoded = base64.b64encode(url.encode('utf-8'))
    
    short_code = make_short_url(7)
    
    database = sqlite3.connect(join(getcwd(), "database.db"))
    cur = database.cursor()
    print(f"INSERT INTO urls (short_url, long_url, timestamp) VALUES ('{str(short_code)}', {str(encoded)[1:]}, {time.time()})")
    cur.execute(f"INSERT INTO urls (short_url, long_url, timestamp) VALUES (?, ?, ?)", (short_code, str(encoded), time.time()))
    
    database.commit()
    
    database.close()
    
    return f"{short_code}"

app.run()