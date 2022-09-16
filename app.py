import sqlite3
from flask import Flask, flash, redirect, render_template, request, jsonify
import random

conn = sqlite3.connect("advancedict.db")
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM words")
words = cursor.fetchall()

app = Flask(__name__)

@app.route("/")
def index():
     a = random.randint(0, 110000)
     random_word = words[a]

     return render_template("index.html", random_word=random_word)

@app.route("/search", methods=['post', 'get'])
def search():
     if request.method == "POST":
          conn = sqlite3.connect("advancedict.db")
          cursor = conn.cursor()
          search = request.form.get('search')
          found = cursor.execute(f"SELECT * FROM words where word LIKE '{search}%' LIMIT 100")
          return render_template("found.html", found=found)
     return render_template("search.html")

@app.route("/word/<query>")
def word(query):
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     found_word = cursor.execute(f"SELECT * FROM words WHERE word == '{query}'")
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
     selected_words = []
     for i in range(10):
          selected_words.append(words[i+int(query)])
     return jsonify({"selected_words": selected_words})

@app.route("/autocorrect", methods=['post', 'get'])
def autocorrect():
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     cursor.execute(f"SELECT word FROM words")
     cwords = cursor.fetchall()
     if request.method == "POST":
          text = request.form.get('text').lstrip()
          split_text = text.split()
          for i in split_text:
               if i not in cwords:
                    try:
                         i = cursor.execute(f"SELECT word FROM words WHERE word LIKE '%{i[len(i)//2:]}' LIMIT 1")[0]
                         i = cursor.execute(f"SELECT word FROM words WHERE word LIKE '%{i[:len(i)//2]}' LIMIT 1")[0]
                         print(i[len(i)/2:len(i)])
                         print(i[0:len(i)/2])
                    except:
                         pass
          print(split_text)
          return redirect("/")
     else:
          return render_template("autocorrect.html")
