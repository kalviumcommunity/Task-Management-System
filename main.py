# Import necessary libraries for working with databases and hashing passwords
import hashlib
import os

# Define the User class
class User:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.__salt = self.__generate_salt()  # Make salt private
        self.__password = self.__hash_password(password)  # Make password private
        self.email = email

    def __hash_password(self, password):  # Make hash_password private
        salted_password = password.encode() + self.__salt
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password

    def __generate_salt(self, length=16):  # Make generate_salt private
        salt_bytes = os.urandom(length)
        return salt_bytes

    def get_user_info(self):  # Provide an abstraction to access user info
        return {
            "User ID": self.user_id,
            "Username": self.username,
            "Email": self.email
        }

class Task:
    def __init__(self, task_id, user_id, task_description):
        self.task_id = task_id
        self.user_id = user_id
        self.task_description = task_description

# Define the TaskStatus class
class TaskStatus:
    def __init__(self, task_id, status):
        self.task_id = task_id
        self.status = status

# Define the TaskDetails class
class TaskDetails:
    def __init__(self, task_id, due_date, priority, archived):
        self.task_id = task_id
        self.due_date = due_date
        self.priority = priority
        self.archived = archived

# Sample usage:

# Create a User object with user input
user_id = int(input("Enter User ID: "))
username = input("Enter Username: ")
password = input("Enter Password: ")
email = input("Enter Email: ")
user1 = User(user_id, username, password, email)

# Create an array to store Task objects
tasks = []

# Create multiple Task objects with user input
num_tasks = int(input("Enter the number of tasks: "))
for _ in range(num_tasks):
    task_id = int(input("Enter Task ID: "))
    task_description = input("Enter Task Description: ")
    task = Task(task_id, user_id, task_description)
    tasks.append(task)

# Create an array to store TaskStatus objects
task_statuses = []

# Create multiple TaskStatus objects with user input
for task in tasks:
    status = input(f"Enter Task Status for Task ID {task.task_id}: ")
    task_status = TaskStatus(task.task_id, status)
    task_statuses.append(task_status)

# Create an array to store TaskDetails objects
task_details_list = []

# Create multiple TaskDetails objects with user input
for task in tasks:
    due_date = input(f"Enter Due Date for Task ID {task.task_id}: ")
    priority = input(f"Enter Priority for Task ID {task.task_id}: ")
    archived = input(f"Enter Archived (Yes/No) for Task ID {task.task_id}: ")
    task_details = TaskDetails(task.task_id, due_date, priority, archived)
    task_details_list.append(task_details)

# Display User information
print("\nUser Information:")
user_info = user1.get_user_info()
for key, value in user_info.items():
    print(f"{key}: {value}")

# Display Task information for each task in the array
print("\nTask Information:")
for task in tasks:
    print(f"Task ID: {task.task_id}")
    print(f"User ID: {task.user_id}")
    print(f"Task Description: {task.task_description}")

# Display TaskStatus information for each task in the array
print("\nTask Status Information:")
for task_status in task_statuses:
    print(f"Task ID: {task_status.task_id}")
    print(f"Status: {task_status.status}")

# Display TaskDetails information for each task in the array
print("\nTask Details Information:")
for task_details in task_details_list:
    print(f"Task ID: {task_details.task_id}")
    print(f"Due Date: {task_details.due_date}")
    print(f"Priority: {task_details.priority}")
    print(f"Archived: {task_details.archived}")
