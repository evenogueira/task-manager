import json

def read_tasks(path="tasks.json"):
    with open(path, "r") as file:
        tasks = json.load(file)
    return tasks

def write_tasks(tasks, path="tasks.json"):
    with open(path, "w") as file:
        json.dump(tasks,file, indent=4,ensure_ascii=False)