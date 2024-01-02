#!/usr/bin/python3
"""The module is meant for dictionary"""
import requests
import json


def get_all_employees_todo_progress():
    # Define the API endpoint URL for users
    users_url = "https://jsonplaceholder.typicode.com/users"

    # Make a GET request to the users endpoint
    users_response = requests.get(users_url)

    # Check if the request was successful (status code 200)
    if users_response.status_code == 200:
        users = users_response.json()

        # Create a dictionary to store TODO information for all employees
        all_employees_todo = {}

        # Iterate over each user to fetch their TODO list
        for user in users:
            user_id = user['id']

            # Define the API endpoint URL for TODOs
            todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

            # Make a GET request to the TODOs endpoint
            todos_response = requests.get(todos_url)

            # Check if the request for TODOs was successful
            if todos_response.status_code == 200:
                todos = todos_response.json()

                # Extract relevant information for each TODO
                todo_list = [
                    {
                        "username": user['name'],
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                    for todo in todos
                ]

                # Add the TODO list to the dictionary
                all_employees_todo[user_id] = todo_list
            else:
                print(f"Error: Unable to fetch TODO list for employee ID {user_id}")

        # Create a JSON file for all employees
        filename = "todo_all_employees.json"
        with open(filename, mode='w') as json_file:
            json.dump(all_employees_todo, json_file, indent=2)

            # print(f"JSON file '{filename}' has been created successfully.")
    else:
        print("Error: Unable to fetch user information.")


if __name__ == "__main__":
    """Call the function to get and export TODO list progress
    for all employees in JSON format
    """
    get_all_employees_todo_progress()
