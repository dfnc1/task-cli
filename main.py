import sys
import json
import datetime as dt

def load_file() -> list[dict]:
    package = "package.json"
    try:
        with open(package) as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = []
    return data

def save_file(new_task: list[dict]) -> None:
    package = "package.json"
    with open(package, "w") as file:
        json.dump(new_task,file,indent=4)

def duplicate_id(tasks: list[dict]) -> int:
    if tasks:
        return tasks[-1]['id']
    else:
        return 0

def create_task(last_id: int, value: str) -> dict:
    return  {
        'id': last_id + 1,
        'description': value,
        'status': 'todo',
        'createAt': dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S'),
        'updateAt': '',
    }

def add_task(value_1: str) -> None:
    tasks = load_file()
    last_id = duplicate_id(tasks)
    new_task = create_task(last_id, value_1)
    tasks.append(new_task)
    save_file(tasks)

def update_task(value_1: str, value_2: str) -> None:
    tasks = load_file()
    for task in tasks:
        if task['id'] == int(value_1):
            task['description'] = value_2
            task['updateAt'] = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d %H:%M:%S')
    save_file(tasks)

def delete_task(value_1: str) -> None:
    tasks = load_file()
    new_task = [task for task in tasks if task["id"] != int(value_1)]
    save_file(new_task)


def list_task(value_1: str) -> None:
    tasks = load_file()
    if value_1 != None:
        for task in tasks:
            if task['status'] == value_1:
                print(task)
    else:
        for task in tasks:
            print(task)

def mark_task(value_1: str, mark: bool) -> None:
    tasks = load_file()
    for task in tasks:
        if task['id'] == int(value_1):
            task['status'] = "in-progress" if mark else "done"
    save_file(tasks)

def main(command: str, value_1: str, value_2: str) -> None:
    match command:
        case "add":
            add_task(value_1)
            print("adding task")

        case "update":
            update_task(value_1, value_2)
            print("deleting task")

        case "delete":
            delete_task(value_1)
            print("deleting task")

        case "list":
            list_task(value_1)
            print("listing tasks")

        case "mark-in-progress":
            mark_task(value_1, True)
            print("mark-in-progress")

        case "mark-done":
            mark_task(value_1, False)
            print("mark-done")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: task-tracker-cli <command> [<args>...]")
        exit(1)
    package = "package.json"
    args = sys.argv[1:]
    command = args[0] if len(args) > 0 else None
    value_1 = args[1] if len(args) > 1 else None
    value_2 = args[2] if len(args) > 2 else None
    main(command, value_1, value_2)