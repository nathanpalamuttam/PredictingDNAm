import csv

# Specify the input and output file names
input_file = 'C://ProgramData/MySQL/MySQL Server 8.0/Uploads/Book6.csv'
output_file = 'roundedvalues.csv'

# Define the rounding function
def round_value(value, decimals=6):
    return round(float(value), decimals)

# Open the input file for reading and the output file for writing
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    next(reader)
    writer = csv.writer(file_out)

    # Iterate over each row in the input file
    for row in reader:
        rounded_row = [round_value(value) for value in row]
        writer.writerow(rounded_row)

# Print a message upon successful completion
print('Rounding completed. Rounded values are saved in', output_file)