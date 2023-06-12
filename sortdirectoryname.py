import os
import csv

def sort_dir():
    def read_csv_into_list(csv_file):
        data = []
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data

    def write_list_to_csv(csv_file, data):
        with open(csv_file, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

    # Specify the directory path
    directory_path = 'Training_images'
    csv_file = 'Book1.csv'  # Replace with the path to your CSV file

    # Get the list of files in the directory without the extension
    file_names = [os.path.splitext(file_name)[0] for file_name in os.listdir(directory_path)]

    # Sort the file names
    sorted_file_names = sorted(file_names)

    # Read the CSV data
    csv_data = read_csv_into_list(csv_file)

    # Create a dictionary to store the index of each file name
    file_index_dict = {file_name: index for index, file_name in enumerate(sorted_file_names)}

    # Update the CSV file with the sorted data
    updated_csv_data = []

    # Add the header row
    updated_csv_data.append(["index", "criminal_name", "Phone no", "Adhaar", "Criminal Activities"])

    # Iterate over the file names and add the corresponding row from the CSV data
    for file_name in sorted_file_names:
        csv_row = [str(file_index_dict[file_name]), file_name, "", "", ""]  # Default empty row

        # Check if the file exists in the CSV data
        for row in csv_data[1:]:
            if row[1] == file_name:
                csv_row = row
                break

        updated_csv_data.append(csv_row)

    # Save the updated data to the CSV file
    write_list_to_csv(csv_file, updated_csv_data)

    # Print the rows that are not present in the file names
    missing_rows = [row for row in csv_data[1:] if row[1] not in sorted_file_names]
    for row in missing_rows:
        print('This Criminal face is not in the directory',row)

# Call the sort_dir function
sort_dir()
