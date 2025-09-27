import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date.strftime("Current date and time: %Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.datetime.now()
    future_date = today + datetime.timedelta(days=number_of_days)
    print(future_date.strftime("Future date: %Y-%m-%d"))
