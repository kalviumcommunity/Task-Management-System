# Import necessary libraries for working with databases and hashing passwords
import hashlib
import os

# Define the User class
class User:
    def __init__(self, user_id, username, password, email):
        self.user_id = user_id
        self.username = username
        self.salt = self.generate_salt()  # Generate a salt for this user
        self.password = self.hash_password(password)  # Hash the password using the salt
        self.email = email

    def hash_password(self, password):
        # Hash the password using the user's salt
        salted_password = password.encode() + self.salt
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password

    def generate_salt(self, length=16):
        # Generate a random salt as bytes
        salt_bytes = os.urandom(length)
        return salt_bytes

# Define the Task class
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
print(f"User ID: {user1.user_id}")
print(f"Username: {user1.username}")
print(f"Email: {user1.email}")

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