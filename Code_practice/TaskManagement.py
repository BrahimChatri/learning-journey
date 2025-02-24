import json,os
import time
from typing import Any

# decorator to count the tasks after adding
def task_count_decorator(func):
    def wrapper(self, task):# -> Any:
        # Call the original function (add_task)
        result = func(self, task)
        # Count the tasks after adding
        print(f"You now have {len(self.tasks)} tasks.")
        return result
    return wrapper

# Class to manage the Task manager
class TaskManager:
    def __init__(self,) -> None:
        self.tasks:list[str|Any] = []

    @task_count_decorator
    def add_task(self, task: str) -> None:
        task_dict = {"task": task, "completed": False,"task_id": len(self.tasks)+1}
        self.tasks.append(task_dict)
        print(f"Task added: {task}")
    
    def view_task(self) -> None:
        for task in self.tasks:
            print(f"{task['task_id']}. {task['task']} - {'Completed' if task['completed'] else 'Not completed'}")
        
    def mark_completed(self, task_id: int) -> None:
        for task in self.tasks:
            if task['task_id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")


    def delet_task(self, task_id: int) -> None:
        for task in self.tasks:
            if task["task_id"] == int(task_id):
                self.tasks.remove(task)
                print(f"{task["task"]} has been removed successfully")
                return
        else:
            print("Task not found !")


    def save_tasks(self, filename:str) -> None:
        tasks_json ={"tasks": self.tasks}
        with open(filename,"w")as f:
            json.dump(tasks_json,f , indent=4)
            print(f"tasks saved to {filename} successfully ")

    def load_tasks(self, filename:str) -> None:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                try:
                    loaded_tasks = json.load(f)
                    self.tasks=loaded_tasks["tasks"]
                except json.JSONDecodeError:
                    print("The tasks file is empty or corrupted. Starting with an empty task list.")
                    self.tasks=[]
        else :
            self.tasks=[]
            print("No task file found. Starting with an empty task list.")

# Function to print text slowly
def print_slow(text:str, delay=0.04):
    for char in text:
        print(char, sep="",end="")
        time.sleep(delay)

def main():
    tasks = TaskManager()
    tasks.load_tasks("tasks.json")  # Load tasks at the start

    while True:
        print(
            """
    ------------------------------
    | 1. Add a task              |
    |----------------------------|
    | 2. View tasks              |
    |----------------------------|
    | 3. Mark task as completed  |
    |----------------------------|
    | 4. Delete task             |
    |----------------------------|
    | 5. Save tasks              |
    |----------------------------|
    | 6. Exit                    |
    ------------------------------   
"""
        )
        print_slow("Enter your choice: ")
        choice = int(input())

        if choice == 6:
            tasks.save_tasks("tasks.json")  # Save tasks on exit
            break
        elif choice == 1:
            task_to_add: str = input("Enter a task to add: ")
            tasks.add_task(task_to_add.strip())
        elif choice == 2:
            tasks.view_task()
        elif choice == 3:
            tasks.view_task()  # Display tasks with IDs
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                tasks.mark_completed(task_id)
            except ValueError:
                print("Invalid task ID, please enter a number.")
        elif choice == 4:
            tasks.view_task()  # Display tasks with IDs
            try:
                task_id = int(input("Enter task ID to remove: "))
                tasks.delet_task(task_id)
            except ValueError:
                print("Invalid task ID, please enter a number.")
        elif choice == 5:
            tasks.save_tasks("tasks.json")


if __name__=="__main__":
    main()