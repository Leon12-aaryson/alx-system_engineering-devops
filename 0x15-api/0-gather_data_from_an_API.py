#!/usr/bin/python3
"""This is the first API task to fetch data"""
import requests
import sys


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

            # Filter completed tasks
            completed_tasks = [todo for todo in todos if todo['completed']]

            # Display progress information
            number_of_done_tasks = len(completed_tasks)
            total_number_of_tasks = len(todos)

            # print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")

            # Display completed task titles
            for task in completed_tasks:
                print(f"\t{task['title']}")
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

        # Call the function to get and display TODO list progress
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
