# PERSONAL TASK MANAGER
# This combines variables, functions, lists, dictionaries, loops, and file I/O

import json
from datetime import datetime

class TaskManager:
    def __init__(self):
        """Initialize the task manager with an empty task list."""
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, priority="medium"):
        """Add a new task to the list."""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority.lower(),
            "completed": False,
            "created_date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added: '{description}' (Priority: {priority})")

    def view_tasks(self, show_completed=False):
        """Display all tasks or filter by completion status."""
        if not self.tasks:
            print("📝 No tasks found. Add some tasks to get started! ")
            return

        print("\n" + "="*60)
        print("📋 YOUR TASKS")
        print("="*60)

        filtered_tasks = self.tasks
        if not show_completed:
            filtered_tasks = [task for task in self.tasks if not task["completed"]]

        if not filtered_tasks:
            status = "completed" if show_completed else "pending"
            print(f"No {status} tasks found.")
            return

        # Sort by priority (high -> medium -> low)
        priority_order = {"high": 1, "medium": 2, "low": 3}
        filtered_tasks.sort(key=lambda x: priority_order.get(x["priority"], 4))

        for task in filtered_tasks:
            status = "✅" if task["completed"] else "⏳"
            priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task["priority"], "⚪")

            print(f"{status} [{task['id']}] {priority_emoji} {task['description']}")
            print(f"    Created: {task['created_date']} | Priority: {task['priority'].title()}")
            print()

    def complete_task(self, task_id):
        """Mark a task as completed."""
        task = self.find_task_by_id(task_id)
        if task:
            if task["completed"]:
                print(f"⚠️  Task '{task['description']}' is already completed!")
            else:
                task["completed"] = True
                task["completed_date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                self.save_tasks()
                print(f"🎉 Task completed: '{task['description']}'")
        else:
            print(f"❌ Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"🗑️  Task deleted: '{task['description']}'")
        else:
            print(f"❌ Task with ID {task_id} not found.")

    def find_task_by_id(self, task_id):
        """Find a task by its ID."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def get_stats(self):
        """Display task statistics."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task["completed"])
        pending_tasks = total_tasks - completed_tasks

        priority_counts = {"high": 0, "medium": 0, "low": 0}
        for task in self.tasks:
            if not task["completed"]:
                priority_counts[task["priority"]] = priority_counts.get(task["priority"], 0) + 1

        print("\n" + "="*40)
        print("📊 TASK STATISTICS")
        print("="*40)
        print(f"Total Tasks: {total_tasks}")
        print(f"Completed: {completed_tasks}")
        print(f"Pending: {pending_tasks}")

        if pending_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100
            print(f"Completion Rate: {completion_rate:.1f}%")
            print("\nPending Tasks by Priority:")
            print(f"  🔴 High: {priority_counts['high']}")
            print(f"  🟡 Medium: {priority_counts['medium']}")
            print(f"  🟢 Low: {priority_counts['low']}")

    def save_tasks(self):
        """Save tasks to a JSON file."""
        try:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file, indent=2)
        except Exception as e:
            print(f"⚠️  Error saving tasks: {e}")

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("📁 No existing task file found. Starting fresh!")
        except Exception as e:
            print(f"⚠️  Error loading tasks: {e}")

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("🎯 PERSONAL TASK MANAGER")
    print("="*50)
    print("1. Add Task")
    print("2. View Pending Tasks")
    print("3. View All Tasks")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. View Statistics")
    print("7. Exit")
    print("-" * 50)

def get_user_input(prompt, input_type=str, valid_options=None):
    """Get user input with validation."""
    while True:
        try:
            user_input = input(prompt)

            # Convert to appropriate type
            if input_type == int:
                user_input = int(user_input)

            # Check if input is in valid options (if provided)
            if valid_options and user_input not in valid_options:
                print(f"Invalid option. Please choose from: {valid_options}")
                continue

            return user_input

        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            exit()

def main():
    """Main program loop."""
    task_manager = TaskManager()

    print("🚀 Welcome to your Personal Task Manager!")
    print("Let's help you stay organized and productive!")

    while True:
        display_menu()

        choice = get_user_input(
            "Choose an option (1-7): ", 
            int, 
            [1, 2, 3, 4, 5, 6, 7]
        )

        if choice == 1:
            # Add Task
            description = get_user_input("Enter task description: ")
            priority = get_user_input(
                "Enter priority (high/medium/low) [default: medium]: "
            ) or "medium"

            if priority.lower() not in ["high", "medium", "low"]:
                print("Invalid priority. Using 'medium' as default.")
                priority = "medium"

            task_manager.add_task(description, priority)

        elif choice == 2:
            # View Pending Tasks
            task_manager.view_tasks(show_completed=False)

        elif choice == 3:
            # View All Tasks
            task_manager.view_tasks(show_completed=True)

        elif choice == 4:
            # Complete Task
            task_manager.view_tasks(show_completed=False)
            if task_manager.tasks:
                task_id = get_user_input("Enter task ID to complete: ", int)
                task_manager.complete_task(task_id)

        elif choice == 5:
            # Delete Task
            task_manager.view_tasks(show_completed=True)
            if task_manager.tasks:
                task_id = get_user_input("Enter task ID to delete: ", int)
                confirm = get_user_input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    task_manager.delete_task(task_id)
                else:
                    print("❌ Deletion cancelled.")

        elif choice == 6:
            # View Statistics
            task_manager.get_stats()

        elif choice == 7:
            # Exit
            print("💾 Saving your tasks...")
            task_manager.save_tasks()
            print("👋 Thank you for using Personal Task Manager!")
            print("🎯 Stay productive and achieve your goals!")
            break

# Enhanced features you can add later:
def future_enhancements():
    """
    Ideas for improving your task manager:

    1. Due dates and reminders
    2. Task categories/tags
    3. Search and filter functionality
    4. Task dependencies
    5. Export to different formats (CSV, TXT)
    6. Task notes and descriptions
    7. Recurring tasks
    8. Time tracking
    9. Task prioritization algorithms
    10. Integration with calendar apps
    """
    pass

if __name__ == "__main__":
    main()

# =============================================================================
# HOW TO RUN THIS PROJECT:
# =============================================================================
# 1. Save this code to a file called 'task_manager.py'
# 2. Open terminal/command prompt
# 3. Navigate to the folder containing the file
# 4. Run: python task_manager.py
# 5. Follow the menu prompts to manage your tasks!
#
# Features included:
# ✅ Add tasks with priorities
# ✅ View pending and completed tasks
# ✅ Mark tasks as complete
# ✅ Delete tasks
# ✅ Task statistics
# ✅ Data persistence (saves to JSON file)
# ✅ Error handling and input validation
# ✅ Clean, user-friendly interface
# =============================================================================
