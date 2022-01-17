from ast import Num
import numbers
from flask import Flask, request, jsonify
import os
from json import load, loads, dump, dumps



app = Flask(__name__)
if(__name__ == '__main__'):
    app.run()

@app.get('/user')
def get_users():
    try:
        os.mkdir('app/database')
        os.system('touch app/database/database.json')
        with open(f"./app/database/database.json", "a") as f:
            f.write('{"data": []}')
        with open(f"./app/database/database.json", "r") as r:
                read = r.read()
        return read, 200

    except FileExistsError:
        with open(f"./app/database/database.json", "r") as r:
            read = r.read()
        if(read == ''):
            with open(f"./app/database/database.json", "a") as f:
                f.write('{"data": []}')
            with open(f"./app/database/database.json", "r") as r:
                read_again = r.read()
                return read_again, 200
        elif(read == '[]'):
            return read, 200
        else:
            with open(f"./app/database/database.json", "r") as r:
                read = load(r)
                return (read), 200


@app.post('/user')
def post_user():
    read = ''
    try:
        with open("./app/database/database.json", "r") as r:
            read = load(r)
    except FileNotFoundError:
        os.mkdir('app/database')
        os.system('touch app/database/database.json')
        with open(f"./app/database/database.json", "a") as f:
            f.write('{"data": []}')
        with open("./app/database/database.json", "r") as r:
            read = load(r)


    if(type(request.get_json()['nome']) != str and type(request.get_json()['email']) != str):
        return {
        "wrong fields": [
        {
            "nome": f"{type(request.get_json()['nome'])}"
        },
        {
            "email": f"{type(request.get_json()['email'])}"
        }
        ]
        }
    elif(type(request.get_json()['nome']) != str):
        return {
        "wrong fields": [
        {
            "nome": f"{type(request.get_json()['nome'])}"
        },
        {
            "email": f"string - correct"
        }
        ]
        }
    elif (type(request.get_json()['email']) != str):
        return {
        "wrong fields": [
        {
            "nome": f"string - correct"
        },
        {
            "email": f"{type(request.get_json()['email'])}"
        }
        ]
        }

    nome = request.get_json()['nome'] 
    email = request.get_json()['email'] 

    formated_name = ''
    formated_email = email.lower()

    for word in nome.split(' '):
        word.lower()
        if(len(nome.split(' ')) != len(formated_name.split(' '))):
            formated_name += word.capitalize() + ' '
        else:
            formated_name += word.capitalize()

    formated_user_data = {'nome': f'{formated_name}', 'email': f'{formated_email}'}



    for data in read['data']:
        if(data['email'] == formated_email):
            return {"error": "User already exists."}, 409
    with open("./app/database/database.json", "w") as w:
        read['data'].append(formated_user_data)
        dump(read, w ,indent=4)
        return {
                "data": formated_user_data
                }, 201




    
