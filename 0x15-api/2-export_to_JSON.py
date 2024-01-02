#!/usr/bin/python3
"""The module below is to export json filesof API"""
import requests
import sys
import json


def get_employee_todo_progress(employee_id):
    """Define the API endpoint URL for TODOs"""
    todos_url = f"https://jsonplaceholder.typicode.com/"\
                f"todos?userId={employee_id}"

    todos_response = requests.get(todos_url)

    if todos_response.status_code == 200:
        todos = todos_response.json()

        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)

        if user_response.status_code == 200:
            user_data = user_response.json()
            employee_name = user_data['name']

            employee_json = {
                "USER_ID": [
                    {
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": employee_name
                    }
                    for todo in todos
                ]
            }

            filename = f"{employee_id}.json"
            with open(filename, mode='w') as json_file:
                json.dump(employee_json, json_file, indent=2)

                """print(f"JSON file '{filename}' has been created
                successfully.")"""
        else:
            print(f"Error: Unable to fetch user information for employee ID "
                  f"{employee_id}")
    else:
        print(f"Error: Unable to fetch TODO list for employee ID "
              f"{employee_id}")


if __name__ == "__main__":
    """Check if an employee ID is provided as a command-line argument"""
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])

        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
