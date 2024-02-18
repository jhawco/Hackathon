import geopy
import csv

# Replace with the path to your CSV file
csv_file_path = "ToiletLocation.csv"

# Open the CSV file
with open(csv_file_path, 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Iterate through each row
    for row in csv_reader:
        # Do something with each row
        print(row)
        









    