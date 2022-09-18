import sqlite3
from flask import Flask, flash, redirect, render_template, request, jsonify
import random
from operation import *

conn = sqlite3.connect("advancedict.db")
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM words")
words = cursor.fetchall()

app = Flask(__name__)

@app.route("/")
def main():
     random_word = get_random()
     return render_template("index.html", random_word=random_word)

@app.route("/search", methods=['post', 'get'])
def search():
     if request.method == "POST":
          search = request.form.get('search')
          found = find_word(search)
          return render_template("found.html", found=found)
     return render_template("search.html")

@app.route("/word/<query>")
def word(query):
     found_word = select_word(query)
     a = 0
     word_list = []
     word2 = ""
     for i in found_word:
          word_list.append(i)
          a+=1
     if a == 1:
          word1 = word_list[0]
     else:
          word1 = word_list[0]
          word2 = word_list[1]
     return render_template('word.html', word=word1, second=word2)

@app.route("/api/<query>")
def api(query):
     selected_words = list_words(query)
     return jsonify({"selected_words": selected_words})