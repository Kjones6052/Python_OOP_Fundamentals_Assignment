# Task 2: Event Management System Enhancement
# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a 
# method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
#     class Event:
#         def __init__(self, name, date):
#             self.name = name
#             self.date = date

class Event:
    def __init__(self):
        self.count = 0
        self.participants = []

    def add_participant(self, name):
        self.participants.append(name)
        self.count += 1

    def get_participant_count(self):
        return self.count

event = Event()

while True:
    action = input("Enter an action (add, count, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter participant name: ")
            event.add_participant(name)
        elif action == "count":
            print(event.get_participant_count())
    except Exception as e:
        print(f"Error occurred: {e}")