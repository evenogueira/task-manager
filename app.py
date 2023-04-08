from flask import request, Flask, Response,jsonify
from models import read_tasks,write_tasks
import json

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_task():
    tasks = read_tasks()
    return Response(json.dumps(tasks,ensure_ascii=False), content_type="application/json; charset=utf-8"),200



@app.route("/create-task",methods=["POST"])
def create_task():
    data = request.get_json()
    tasks = read_tasks()

    new_task = {
        "id": len(tasks)+1,
        "titulo":data.get("titulo"),
        "descricao": data.get("descricao"),
        "completa": False
    }

    tasks.append(new_task)

    write_tasks(tasks)

    return Response(json.dumps(new_task,ensure_ascii=False), content_type="application/json; charset=utf-8"),201

@app.route("/complete_task/<int:id>",methods=["DELETE"])
def delete_task(id):
    tasks = read_tasks()
    for task in tasks:
        if task["id"]==id:
            task.update({"completa:True"})
    write_tasks(tasks )
    
    return jsonify({}),204



if __name__ == '__main__':
    app.run(debug=True)