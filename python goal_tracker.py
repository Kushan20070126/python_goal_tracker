import json

# File to store goals and tasks
FILE_NAME = "goals.json"

# Function to load goals from file
def load_goals():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save goals to file
def save_goals(goals):
    with open(FILE_NAME, "w") as file:
        json.dump(goals, file, indent=4)

# Function to add a new goal
def add_goal(goals):
    goal_name = input("Enter your goal: ")
    goals[goal_name] = []
    print(f"Goal '{goal_name}' added.")
    return goals

# Function to add tasks to a goal
def add_task(goals):
    goal_name = input("Enter the goal to add tasks to: ")
    if goal_name in goals:
        task = input("Enter the task: ")
        deadline = input("Enter the deadline (e.g., YYYY-MM-DD): ")
        goals[goal_name].append({"task": task, "deadline": deadline, "completed": False})
        print(f"Task '{task}' added to goal '{goal_name}'.")
    else:
        print(f"Goal '{goal_name}' not found.")
    return goals

# Function to mark a task as completed
def complete_task(goals):
    goal_name = input("Enter the goal: ")
    if goal_name in goals:
        for i, task in enumerate(goals[goal_name], 1):
            print(f"{i}. {task['task']} (Deadline: {task['deadline']}) - Completed: {task['completed']}")
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(goals[goal_name]):
            goals[goal_name][task_num]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    else:
        print(f"Goal '{goal_name}' not found.")
    return goals

# Function to view goals and tasks
def view_goals(goals):
    if goals:
        for goal, tasks in goals.items():
            print(f"\nGoal: {goal}")
            for i, task in enumerate(tasks, 1):
                status = "✔️" if task["completed"] else "❌"
                print(f"  {i}. {task['task']} (Deadline: {task['deadline']}) - Status: {status}")
    else:
        print("No goals found.")

# Main menu
def main():
    goals = load_goals()
    while True:
        print("\n--- Goal Tracker ---")
        print("1. Add a Goal")
        print("2. Add a Task to a Goal")
        print("3. Mark Task as Completed")
        print("4. View Goals and Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            goals = add_goal(goals)
        elif choice == "2":
            goals = add_task(goals)
        elif choice == "3":
            goals = complete_task(goals)
        elif choice == "4":
            view_goals(goals)
        elif choice == "5":
            save_goals(goals)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
