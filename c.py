import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Open the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # Read the CSV file
        csv_reader = csv.DictReader(csv_file)

        # Convert each row into a dictionary and add it to the list
        for row in csv_reader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"CSV file {csv_file_path} successfully converted to JSON file {json_file_path}")

# Example usage
csv_file_path = 'example.csv'  # Replace with your CSV file path
json_file_path = 'output.json'  # Replace with your desired JSON output path

csv_to_json(csv_file_path, json_file_path)
