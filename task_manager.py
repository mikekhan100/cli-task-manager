"""
CLI Task Manager
"""

# Module imports
import json
import os
from datetime import datetime

# Store the tasks in memory while the program is running
tasks = []

# File to save tasks
TASKS_FILE = "tasks.json"

# Priority levels
PRIORITY_LEVELS = {
    "1": "High",
    "2": "Medium",
    "3": "Low"
}

def load_tasks():
    """Load tasks from JSON file if it exists"""
    global tasks    # Allows modification of the tasks variable which is declared outside the function

    # Handle missing or corrupted file gracefully
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                tasks = json.load(file)
                print(f"✓ Loaded {len(tasks)} task(s)")
        except json.JSONDecodeError:
            print("⚠ Error reading tasks file, starting afresh")
            tasks = []
    else:
        print("No existing tasks found, starting afresh")
        tasks = []


def save_tasks():
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)


def add_task():
    """Add a new task to the list"""
    description = input("Enter task description: ").strip()

    if not description:
        print("⚠ Task description cannot be empty")
        return
    
    # Ask for priority level
    print("\nSelect priority level:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority_choice = input("Enter priority level (1-3), default is Medium: ").strip()

    # Validate priority choice - if invalid, set to Medium
    if priority_choice not in PRIORITY_LEVELS:
        priority_choice = "2"  # Default to Medium
        print("⚠ Invalid priority choice, setting default to Medium")

    priority = PRIORITY_LEVELS[priority_choice]

    # Create a task object
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    tasks.append(task)
    save_tasks()
    print(f"✓ Task added successfully! (ID: {task['id']}, Priority: {task['priority']})")


def get_priority_colour(priority):    
    """Return colour code based on priority level"""
    colours = {
        "High": "\033[91m",    # Red
        "Medium": "\033[93m",  # Yellow
        "Low": "\033[92m"      # Green
    }
    reset = "\033[0m"   # Reset colour
    
    colour = colours.get(priority, "")
    return f"{colour}{priority}{reset}"


def view_tasks():
    """Display all tasks"""
    if not tasks:
        print("\nNo tasks yet! Add some to get started.\n")
        return

    print("\n" + "="*60)
    print("YOUR TASKS")
    print("="*60)

    for task in tasks:  # tasks is a list of dictionaries
        status = "✓" if task["completed"] else "○"

        # Get priority with colour
        # Use .get() to avoid KeyError in case of missing priority
        priority = task.get("priority", "Medium")
        priority_coloured = get_priority_colour(priority)

        # Format the output
        print(f"\n[{task['id']}] {status} {task['description']}")
        print(f"    Priority: {priority_coloured}")
        print(f"    Created: {task['created_at']}")

        if task["completed"]:
            print(f"    Completed: {task.get('completed_at', 'N/A')}")
            # task.get() used instead of task["completed_at"] as the latter crashes if
            # "completed_at" is missing

    print("\n" + "="*60 + "\n")


def complete_task():
    """Mark a task as complete"""
    if not tasks:
        print("No tasks to complete!")
        return
    
    try:
        task_id = int(input("Enter task ID to mark as complete: "))

        # Find the task
        task_found = False
        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("⚠ This task is already completed")
                else:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    save_tasks()
                    print(f"✓ Task {task_id} marked as complete!")
                    task_found = True
                    break

        if not task_found:
            print(f"⚠ Task with ID {task_id} not found")

    except ValueError:
        print("⚠ Please enter a valid number")


def delete_task():
    """Delete a task from the list"""
    if not tasks:
        print("No tasks to delete!")
        return
    
    try:
        task_id = int(input("Enter task ID to delete: "))

        # Find and remove the task
        for i, task in enumerate(tasks): # enumerate to obtain index + item
            if task["id"] == task_id:
                tasks.pop(i)    # remove item at index i
                reset_IDs()  # helper function to reset IDs after deletion
                print(f"✓ Task {task_id} deleted")
                return
        
        print(f"⚠ Task with ID {task_id} not found")

    except ValueError:
        print("⚠ Please enter a valid number")


def reset_IDs():
    for i, task in enumerate(tasks):
        task["id"] = i + 1
    save_tasks()
    print("✓ Task IDs reset successfully!")


def show_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("TASK MANAGER")
    print("="*60)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print("="*60)


def main():
    """Main function - the entry point of the program"""
    print("\n🎯 Welcome to Task Manager!\n")
    load_tasks()

    # Main program loop
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\n👋 Thanks for using Task Manager! Goodbye!\n")
            break  # Exit the loop
        else:
            print("⚠ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()