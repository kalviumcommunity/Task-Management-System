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

# Create a Task object with user input
task_id = int(input("Enter Task ID: "))
task_description = input("Enter Task Description: ")
task1 = Task(task_id, user_id, task_description)

# Create a TaskStatus object with user input
status = input("Enter Task Status: ")
task_status1 = TaskStatus(task_id, status)

# Create a TaskDetails object with user input
due_date = input("Enter Due Date: ")
priority = input("Enter Priority: ")
archived = input("Enter Archived (Yes/No): ")
task_details1 = TaskDetails(task_id, due_date, priority, archived)

# Display User information
print("\nUser Information:")
user_info = user1.get_user_info()
for key, value in user_info.items():
    print(f"{key}: {value}")

# Display Task information
print("\nTask Information:")
print(f"Task ID: {task1.task_id}")
print(f"User ID: {task1.user_id}")
print(f"Task Description: {task1.task_description}")

# Display TaskStatus information
print("\nTask Status Information:")
print(f"Task ID: {task_status1.task_id}")
print(f"Status: {task_status1.status}")

# Display TaskDetails information
print("\nTask Details Information:")
print(f"Task ID: {task_details1.task_id}")
print(f"Due Date: {task_details1.due_date}")
print(f"Priority: {task_details1.priority}")
print(f"Archived: {task_details1.archived}")