#from operation import *
import sqlite3
from flask import Flask, flash, redirect, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
     a = random.randint(0, 110000)
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     cursor.execute(f"SELECT * FROM words")
     word = cursor.fetchall()
     random_word = word[a]
     print(random_word)

     return render_template("index.html", random_word=random_word)

@app.route("/")
def search():
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     return render_template("index.html", random_word=random_word)