import csv
import datetime
import os

# Define the input and output file paths
input_file = 'read.csv'
output_file = f"record_{datetime.datetime.now().strftime('%Y_%m_%d')}.csv"

# Check if the output file exists, and create it if it doesn't
if not os.path.exists(output_file):
    with open(output_file, 'w', newline='') as f:
        pass

# Open the input file for reading and the output file for appending
with open(input_file, 'r') as f1, open(output_file, 'a', newline='') as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)

    # Skip the header row in the input file
    next(reader)

    # Loop through each row in the input file
    for row in reader:

        # Get the current date and time
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y_%m_%d %H:%M:%S')

        # Append the timestamp to the current row in the input file
        row.append(timestamp)

        # Write the modified row to the output file with the timestamp
        writer.writerow(row)

print(f'New entries added to {output_file}')
