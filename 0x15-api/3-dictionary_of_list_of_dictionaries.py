#!/usr/bin/python3
"""The module is meant for dictionary"""
import requests
import json


def get_all_employees_todo_progress():
    """Define the API endpoint URL for users"""
    users_url = "https://jsonplaceholder.typicode.com/users"

    users_response = requests.get(users_url)

    if users_response.status_code == 200:
        users = users_response.json()

        all_employees_todo = {}

        for user in users:
            user_id = user['id']

            todos_url = f"https://jsonplaceholder.typicode.com/todos?"\
                f"userId={user_id}"

            todos_response = requests.get(todos_url)

            if todos_response.status_code == 200:
                todos = todos_response.json()

                todo_list = [
                    {
                        user_id: [
                            {
                                "username": user['username'],
                                "task": todo['title'],
                                "completed": todo['completed']
                            }
                        ]
                    }
                    for todo in todos
                ]

                all_employees_todo.update({user_id: todo_list})
            else:
                print(f"Error: Unable to fetch TODO list for employee"
                      f" ID {user_id}")

        filename = "todo_all_employees.json"
        with open(filename, mode='w') as json_file:
            json.dump(all_employees_todo, json_file, indent=2)

        print(f"JSON file '{filename}' has been created successfully.")
    else:
        print("Error: Unable to fetch user information.")


if __name__ == "__main__":
    """Call the function to get and export TODO list progress
    for all employees in JSON format
    """
    get_all_employees_todo_progress()
