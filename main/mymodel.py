import sqlite3
import random
root = '../'

def parse(values):
     parsed = []
     if values != []:
          for i in values:
               out = {}
               out['word'] = i[1]
               out['word_class'] = i[2]
               out['length'] = i[3]
               out['definition'] = i[4]
               parsed.append(out)
               
     return parsed
def query_db(query):
     conn = sqlite3.connect(f"dictionary.db")
     cursor = conn.cursor()
     cursor.execute(f"{query}")
     result = cursor.fetchall()
     return (result)

def get_random():
     words = query_db("SELECT * FROM words")
     out = [list(random.choice(words))]
     return parse(out)

def search_word(search):
     return parse(query_db(f"SELECT * FROM words where word LIKE '{search}%' LIMIT 100"))

def get_word(query):
     return parse(query_db(f"SELECT * FROM words WHERE word == '{query}'"))

def list_words(query):
     try:
          words = query_db("SELECT * FROM words")
          words_list = []
          for i in range(10):
               words_list.append(words[i+int(query)])
          return parse(words_list)
     except:
          return "Invalid Query."
