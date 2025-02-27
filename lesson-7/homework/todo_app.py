# from abc import ABC, abstractmethod

class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.status}"

# class StorageStrategy(ABC):
#     @abstractmethod
#     def save(self, tasks, filename):
#         pass

#     @abstractmethod
#     def load(self, filename):
#         pass

# class CSVStorageStrategy(StorageStrategy):
class CSVStorageStrategy():
    def save(self, tasks, filename):
        with open(filename, mode='w') as file:
            file.write("Task ID,Title,Description,Status\n")
            for task in tasks:
                file.write(f"{task.task_id},{task.title},{task.description},{task.status}\n")

    def load(self, filename):
        tasks = []
        try:
            with open(filename, mode='r') as file:
                lines = file.readlines()[1:]
                for line in lines:
                    task_id, title, description, status = line.strip().split(',')
                    tasks.append(Task(task_id, title, description, status))
        except FileNotFoundError:
            pass
        return tasks

# class JSONStorageStrategy(StorageStrategy):
class JSONStorageStrategy():
    def save(self, tasks, filename):
        with open(filename, mode='w') as file:
            file.write("[\n")
            for i, task in enumerate(tasks):
                file.write(f'{{"task_id": "{task.task_id}", "title": "{task.title}", "description": "{task.description}", "status": "{task.status}"}}')
                if i < len(tasks) - 1:
                    file.write(",\n")
                else:
                    file.write("\n")
            file.write("]")

    def load(self, filename):
        tasks = []
        try:
            with open(filename, mode='r') as file:
                data = file.read().strip()
                if data:
                    data = data[1:-1].strip()
                    if data:
                        items = data.split("}, {")
                        for item in items:
                            item = item.strip("{} ")
                            task_data = {}
                            for pair in item.split(", "):
                                key, value = pair.split(": ")
                                task_data[key.strip('"')] = value.strip('"')
                            tasks.append(Task(task_data["task_id"], task_data["title"], task_data["description"], task_data["status"]))
        except FileNotFoundError:
            pass
        return tasks

class ToDoApp:
    def __init__(self, storage_strategy):
        self.tasks = []
        self.storage_strategy = storage_strategy

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks found.")

    def update_task(self, task_id, title=None, description=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title:
                    task.title = title
                if description:
                    task.description = description
                if status:
                    task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered_tasks = [task for task in self.tasks if task.status == status]
        if filtered_tasks:
            print(f"Tasks with status '{status}':")
            for task in filtered_tasks:
                print(task)
        else:
            print(f"No tasks with status '{status}' found.")

    def save_tasks(self, filename):
        self.storage_strategy.save(self.tasks, filename)
        print("Tasks saved successfully!")

    def load_tasks(self, filename):
        self.tasks = self.storage_strategy.load(filename)
        print("Tasks loaded successfully!")

    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                task_id = input("Enter Task ID: ")
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                status = input("Enter Status (Pending/In Progress/Completed): ")
                task = Task(task_id, title, description, status)
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_id = input("Enter Task ID to update: ")
                title = input("Enter new Title (leave blank to keep current): ")
                description = input("Enter new Description (leave blank to keep current): ")
                status = input("Enter new Status (leave blank to keep current): ")
                self.update_task(task_id, title, description, status)
            elif choice == "4":
                task_id = input("Enter Task ID to delete: ")
                self.delete_task(task_id)
            elif choice == "5":
                status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
                self.filter_tasks(status)
            elif choice == "6":
                filename = input("Enter filename to save tasks: ")
                self.save_tasks(filename)
            elif choice == "7":
                filename = input("Enter filename to load tasks: ")
                self.load_tasks(filename)
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    storage_format = input("Choose storage format (csv/json): ").strip().lower()
    if storage_format == "csv":
        storage_strategy = CSVStorageStrategy()
    elif storage_format == "json":
        storage_strategy = JSONStorageStrategy()
    else:
        print("Invalid storage format. Defaulting to CSV.")
        storage_strategy = CSVStorageStrategy()

    app = ToDoApp(storage_strategy)
    app.menu()