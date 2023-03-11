import json

string_as_json = '{"answer":"Hello, user"}'
obj=json.loads(string_as_json)
print(obj['answer'])
key="answer2"

if key in
    print(obj[key])
else:
    print(f"Ключа {key} в json нет")