import csv
from datetime import datetime, timedelta

def analyze_employee_data(file_path):
    # Assumption: The file is a CSV with columns 'Employee', 'Date', 'Start Time', 'End Time'
    # You may need to adjust this based on the actual structure of your data.

    # Load data from CSV file
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Function to convert time string to datetime object
    def convert_to_datetime(time_str):
        return datetime.strptime(time_str, '%H:%M')

    # Analyze the data
    for row in data:
        # Convert start and end times to datetime objects
        start_time = convert_to_datetime(row['Start Time'])
        end_time = convert_to_datetime(row['End Time'])

        # Calculate shift duration
        shift_duration = end_time - start_time

        # Check conditions and print results
        if shift_duration >= timedelta(days=7):
            print(f"Employee {row['Employee']} has worked for 7 consecutive days.")

        if timedelta(hours=1) < shift_duration < timedelta(hours=10):
            print(f"Employee {row['Employee']} has less than 10 hours between shifts but greater than 1 hour.")

        if shift_duration > timedelta(hours=14):
            print(f"Employee {row['Employee']} has worked for more than 14 hours in a single shift.")

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")
    analyze_employee_data(file_path)
