import sqlite3
import random

def query_db(query):
     conn = sqlite3.connect("advancedict.db")
     cursor = conn.cursor()
     cursor.execute(f"{query}")
     result = cursor.fetchall()
     return (result)

def get_random():
     words = query_db("SELECT * FROM words")
     a = random.randint(0, len(words))
     return words[a]

def find_word(search):
     return query_db(f"SELECT * FROM words where word LIKE '{search}%' LIMIT 100")

def select_word(query):
     return query_db(f"SELECT * FROM words WHERE word == '{query}'")

def list_words(query):
     try:
          words = query_db("SELECT * FROM words")
          words_list = []
          for i in range(10):
               words_list.append(words[i+int(query)])
          return words_list
     except:
          return "Invalid Query."
