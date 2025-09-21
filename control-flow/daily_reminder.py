task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match (priority, time_bound):
    case ("high", "yes") if priority == "high" and time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case ("low", "no") if priority == "low" and time_bound == "no":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
