from flask import Flask, jsonify, request

app = Flask(__name__)

data =[
    {
        "id": 1,
        "name": u' Jeoge Stefnophilis',
        "contact": u'098765322456',
        "done": False
    },
    {
        "id": 2,
        "name":u'Stenphensmen',
        "contact": u'8796546789',
        "done": False
    }
]

@app.route("/")
def hello():
    return "Chowder, Dont try peeing on the floor!!"


@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    



if(__name__ == "__main__"):
    app.run()