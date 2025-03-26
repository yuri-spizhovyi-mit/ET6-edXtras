#!/usr/bin/env python3

print("\nSimple Task Tracker\n")

tasks = []
completed_tasks = 0
pending_tasks = 0

while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Mark task as complete")
    print("3. List tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task_name = input("Enter task name: ")
        task_priority = input("Enter task priority (high/medium/low): ")
        
        tasks.append({
            'name': task_name, 
            'priority': task_priority, 
            'completed': False
        })
        pending_tasks += 1
        print(f"Task '{task_name}' added")

    elif choice == '2':
        if not tasks:
            print("No tasks to mark complete")
            continue

        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['name']} (Priority: {task['priority']})")
        
        try:
            task_index = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= task_index < len(tasks):
                if not tasks[task_index]['completed']:
                    tasks[task_index]['completed'] = True
                    completed_tasks += 1
                    pending_tasks -= 1
                    print(f"Task '{tasks[task_index]['name']}' marked as complete")
                else:
                    print("Task is already complete")
            else:
                print("Invalid task number")
        except ValueError:
            print("Invalid input")

    elif choice == '3':
        if not tasks:
            print("No tasks")
        else:
            print("\nAll Tasks:")
            for task in tasks:
                status = "Completed" if task['completed'] else "Pending"
                print(f"{task['name']} (Priority: {task['priority']}, Status: {status})")

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please try again.")

print("\nTask Summary:")
print(f"Total Tasks: {len(tasks)}")
print(f"Completed Tasks: {completed_tasks}")
print(f"Pending Tasks: {pending_tasks}")
