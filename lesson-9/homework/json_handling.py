import json
import csv

def load_tasks(filename='tasks.json'):
    with open(filename, 'r') as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print(f"{'ID'}, {'Task Name'}, {'Completed'}, {'Priority'}")
    for task in tasks:
        print(f"{task['id']}, {task['task']}, {task['completed']}, {task['priority']}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks

    stats = {
        'Total tasks': total_tasks,
        'Completed tasks': completed_tasks,
        'Pending tasks': pending_tasks,
        'Average priority': average_priority
    }
    return stats

def display_stats(stats):
    for key, value in stats.items():
        print(f"{key}: {value}")

def convert_to_csv(tasks, filename='tasks.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Task', 'Completed', 'Priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })

tasks = load_tasks()

display_tasks(tasks)

stats = calculate_stats(tasks)
display_stats(stats)

save_tasks(tasks)

convert_to_csv(tasks)