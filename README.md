# MyDict 

Access a dictionary with over 100,000 words using rest framework

### Live at: [mydictionary](https://mydictionary.pythonanywhere.com)
### Swagger Documentation at: [mydictionary Documentation](https://mydictionary.pythonanywhere.com/docs)

---

I'm open to collaborations on this project 😊, if you have an idea to improve this project, don't hesitate to fork update and create a pull request (frontend or backend)

---

Sample Request & Response

```GET /get/all```

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "word": "all",
        "word_class": "adjective",
        "length": 3,
        "definition": "Only; alone; nothing but."
    },
    {
        "word": "all",
        "word_class": "adverb",
        "length": 3,
        "definition": "Even; just. (Often a mere intensive adjunct.)"
    },
    {
        "word": "all",
        "word_class": "noun",
        "length": 3,
        "definition": "The whole number, quantity, or amount; the entire thing; everything included or concerned; the aggregate; the whole; totality; everything or every person; as, our all is at stake."
    },
    {
        "word": "all",
        "word_class": "other",
        "length": 3,
        "definition": "Although; albeit."
    }
]
```

