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
    with open("./app/database/database.json", "r") as r:
        read = load(r)['data']
    #     load(r)['data'].append('asd')

    with open("./app/database/database.json", "a") as w:
        dump(str(request.get_json()), read, indent=4, skipkeys=True)
        return '', 200