#!/usr/bin/python3
import requests
import sys
import json


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL for TODOs
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Make a GET request to the TODOs endpoint
    todos_response = requests.get(todos_url)

    # Check if the request was successful (status code 200)
    if todos_response.status_code == 200:
        todos = todos_response.json()

        # Get the user's name from the users endpoint
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        user_response = requests.get(user_url)

        # Check if the request for user information was successful
        if user_response.status_code == 200:
            user_data = user_response.json()
            employee_name = user_data['name']

            # Create a JSON structure for the employee
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

            # Create a JSON file for the employee
            filename = f"{employee_id}.json"
            with open(filename, mode='w') as json_file:
                json.dump(employee_json, json_file, indent=2)

                # print(f"JSON file '{filename}' has been created successfully.")
        else:
            print(f"Error: Unable to fetch user information for employee ID {employee_id}")
    else:
        print(f"Error: Unable to fetch TODO list for employee ID {employee_id}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        # Convert the provided argument to an integer (employee ID)
        employee_id = int(sys.argv[1])

        # Call the function to get and export TODO list progress in JSON format
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
