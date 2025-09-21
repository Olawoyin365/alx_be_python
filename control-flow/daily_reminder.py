task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task "
        if time_bound == "yes":
            message += "that requires immediate attention today!"
    case _:
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
print(message)
