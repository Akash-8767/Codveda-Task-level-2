import json
import os

TO_DO_TASK_FILE = 'tasks.sky'

def load_tasks():
    if not os.path.exists(TO_DO_TASK_FILE):
        return []
    with open(TO_DO_TASK_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TO_DO_TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    Task_Name = input("Enter the Task: ").strip()
    if Task_Name:
        tasks = load_tasks()
        tasks.append({"task": Task_Name, "completed": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print(" Task name cannot be empty.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Task is Not found.")
        return

    print("\n TO DO LIST:")
    for index, task in enumerate(tasks, start=1):
        status = "complete" if task['completed'] else "not complete"
        print(f"{index}. [{status}] {task['task']}")
    print()

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("Enter the number of task which you want to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f" Deleted: {removed['task']}")
        else:
            print("You Enter invalid task number which not mention in task list.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    tasks = load_tasks()
    view_tasks()
    try:
        num = int(input("Enter the number of task which you want to marked as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['completed'] = True
            save_tasks(tasks)
            print(f"Marked the task as complete: {tasks[num - 1]['task']}")
        else:
            print(" You Enter Invalid task number.")
    except ValueError:
        print("You have been Enter ivalid number.")

def main():
    while True:
        print("\n TO DO LIST MENU")
        print("1. ADD")
        print("2. VIEW")
        print("3. DELETE")
        print("4. COMPLETE")
        print("5. RETRUN ")

        choice = input("Enter Your what you want in task list between  (1-5):").strip()

        if choice == '1':
            add_task()

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            delete_task()

        elif choice == '4':
            mark_task_complete()
            
        elif choice == '5':
            print(" Bye bye !!!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()