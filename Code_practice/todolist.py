"Simple to-do-list that uses classes "

import uuid


class Task:
    def __init__(self, description, completed=False):
        self.id = uuid.uuid4()
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(f"ID: {task.id}, Description: {task.description}, Completed: {task.completed}")

    def mark_task_as_completed(self, task_id):
        for task in self.tasks:
            if str(task.id) == task_id:
                task.completed = True
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if str(task.id) == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = input("Enter task ID to mark as completed: ")
            todo_list.mark_task_as_completed(task_id)
        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            todo_list.delete_task(task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

