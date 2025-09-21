task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task "
        if time_bound == "yes":
            reminder += "that requires immediate attention today!"
    case "low":
        reminder = f"Note: '{task}' is a low priority task. "
        if time_bound == "no":
            reminder += "Consider completing it when you have free time."
print(reminder)
