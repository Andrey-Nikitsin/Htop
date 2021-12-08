import json


def open_file(s):
    with open(f'./{s}',encoding='utf-8') as file:
        out=json.load(file)
        print(out)

open_file('log.json')