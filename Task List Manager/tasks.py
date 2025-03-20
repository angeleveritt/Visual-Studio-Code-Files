# Assignment - TaskList Manager - Angelique Everitt
print()
print("Assignment - TaskList Manager")
print()

import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, description="", due_date=None, priority="medium", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def __str__(self):
        status = "✓" if self.completed else "□"
        due_str = f", Due: {self.due_date}" if self.due_date else ""
        priority_indicator = {"low": "⬇", "medium": "⬌", "high": "⬆"}
        priority_icon = priority_indicator.get(self.priority.lower(), "⬌")
        
        return f"[{status}] {priority_icon} {self.title}{due_str}"
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization"""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed,
            "created_date": self.created_date
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a Task object from dictionary data"""
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            priority=data.get("priority", "medium"),
            completed=data.get("completed", False)
        )
        task.created_date = data.get("created_date", datetime.now().strftime("%Y-%m-%d %H:%M"))
        return task


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        """
        Add a new task to the task list
        
        Args:
            title (str): Task title (required)
            description (str): Task description
            due_date (str): Due date in YYYY-MM-DD format
            priority (str): Priority level (low, medium, high)
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Validate inputs
        if not title.strip():
            print("Error: Task title cannot be empty")
            return False
        
        # Validate due date format if provided
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Error: Due date must be in YYYY-MM-DD format")
                return False
        
        # Validate priority
        if priority.lower() not in ["low", "medium", "high"]:
            print("Error: Priority must be 'low', 'medium', or 'high'")
            return False
        
        # Create and add the task
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f"Task added: {title}")
        return True
    
    def remove_task(self, index):
        """
        Remove a task by index
        
        Args:
            index (int): Task index to remove
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                print(f"Removed task: {removed_task.title}")
                return True
            else:
                print("Error: Invalid task index")
                return False
        except Exception as e:
            print(f"Error removing task: {e}")
            return False
    
    def mark_completed(self, index):
        """
        Mark a task as completed
        
        Args:
            index (int): Task index to mark as completed
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if 0 <= index < len(self.tasks):
                self.tasks[index].completed = True
                print(f"Marked as completed: {self.tasks[index].title}")
                return True
            else:
                print("Error: Invalid task index")
                return False
        except Exception as e:
            print(f"Error marking task as completed: {e}")
            return False
    
    def remove_completed_tasks(self):
        """
        Remove all completed tasks from the list
        
        Returns:
            int: Number of tasks removed
        """
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed_count = original_count - len(self.tasks)
        
        if removed_count > 0:
            print(f"Removed {removed_count} completed task(s)")
        else:
            print("No completed tasks to remove")
        
        return removed_count
    
    def view_tasks(self, show_completed=True):
        """
        Display the current task list
        
        Args:
            show_completed (bool): Whether to show completed tasks
        """
        if not self.tasks:
            print("No tasks found")
            return
        
        # Filter tasks based on completion status if needed
        tasks_to_show = self.tasks if show_completed else [t for t in self.tasks if not t.completed]
        
        if not tasks_to_show:
            print("No tasks to display")
            return
        
        print("\nCurrent Tasks:")
        print("-" * 50)
        
        for i, task in enumerate(tasks_to_show):
            print(f"{i}. {task}")
            if task.description:
                print(f"   {task.description}")
        
        print("-" * 50)
        
        # Display task stats
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        print(f"Total: {total} | Completed: {completed} | Remaining: {total - completed}")
    
    def save_tasks(self):
        """
        Save tasks to a JSON file
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Convert tasks to dictionaries
            task_dicts = [task.to_dict() for task in self.tasks]
            
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(task_dicts, file, indent=2)
            
            print(f"Tasks saved to {self.filename}")
            return True
        except PermissionError:
            print(f"Error: Permission denied when saving to {self.filename}")
            return False
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def load_tasks(self):
        """
        Load tasks from a JSON file
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not os.path.exists(self.filename):
            print(f"No task file found. Will create {self.filename} when saving.")
            return False
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                task_dicts = json.load(file)
            
            # Convert dictionaries to Task objects
            self.tasks = [Task.from_dict(task_dict) for task_dict in task_dicts]
            
            print(f"Loaded {len(self.tasks)} tasks from {self.filename}")
            return True
        except json.JSONDecodeError:
            print(f"Error: {self.filename} is not a valid JSON file")
            return False
        except PermissionError:
            print(f"Error: Permission denied when reading {self.filename}")
            return False
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return False


def get_valid_date():
    """Get a valid date from user input"""
    while True:
        date_str = input("Enter due date (YYYY-MM-DD) or leave empty for none: ")
        if not date_str:
            return None
        
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")


def main():
    # Create task manager
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. View all tasks")
        print("2. View active tasks only")
        print("3. Add a new task")
        print("4. Mark a task as completed")
        print("5. Remove a task")
        print("6. Remove all completed tasks")
        print("7. Save tasks")
        print("8. Load tasks")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == '1':
            task_manager.view_tasks()
            
        elif choice == '2':
            task_manager.view_tasks(show_completed=False)
            
        elif choice == '3':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date = get_valid_date()
            
            # Get priority
            print("Priority level:")
            print("1. Low")
            print("2. Medium (default)")
            print("3. High")
            priority_choice = input("Select priority (1-3) or press Enter for Medium: ")
            
            priority_map = {
                "1": "low",
                "2": "medium",
                "3": "high",
                "": "medium"
            }
            priority = priority_map.get(priority_choice, "medium")
            
            task_manager.add_task(title, description, due_date, priority)
            
        elif choice == '4':
            task_manager.view_tasks()
            try:
                index = int(input("Enter the index of the task to mark as completed: "))
                task_manager.mark_completed(index)
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == '5':
            task_manager.view_tasks()
            try:
                index = int(input("Enter the index of the task to remove: "))
                task_manager.remove_task(index)
            except ValueError:
                print("Please enter a valid number")
                
        elif choice == '6':
            task_manager.remove_completed_tasks()
            
        elif choice == '7':
            task_manager.save_tasks()
            
        elif choice == '8':
            task_manager.load_tasks()
            
        elif choice == '9':
            print("Saving tasks before exit...")
            task_manager.save_tasks()
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()

print()
print("fin")
print()

