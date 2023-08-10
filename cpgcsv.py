import csv
import pickle

lists = []


def storeCpGbyGene():
    filepath = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneCpG.csv'
    filename = "output2.csv"
    with open(filepath, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        next(reader)
        listOfGenes = []
        # Iterate over each row in the file
        for row_num, row in enumerate(reader):
            if row[1] not in listOfGenes:
                listOfGenes.append(row[1])
                newList = []
                newList.append(row[1])
                with open(filepath, 'r') as file_inner:
                    reader_inner = csv.reader(file_inner)
                    for _ in range(row_num):
                        next(reader_inner)
                    for newrow in reader_inner:
                        if newrow[1] == row[1]:
                            newList.append(newrow[0])
                    lists.append(newList)
    with open(filename, mode="w", newline="") as file2:
        writer = csv.writer(file2)
        for _ in lists:
            writer.writerow(_)


def cpgGeneCSVTransfer2():
    csv_file = 'C:/Users/npp8/PycharmProjects/pythonProject/output.csv'
    csv_file2 = 'C:/Users/npp8/PycharmProjects/pythonProject/output2.csv'
    result_dict = {}
    # Open the CSV file with key-value pairs
    with open(csv_file2, 'r') as file:
        csv_reader = csv.reader(file)
        # Create an empty dictionary to store the data

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Extract the key (first element in the row)
            key = row[0]

            # Search for the remaining elements in another CSV file
            with open(csv_file, 'r') as search_file:
                search_reader = csv.reader(search_file)
                row_numbers = []

                # Iterate through each row in the search file
                for row_num, search_row in enumerate(search_reader, start=1):
                    # Iterate through each element in the row
                    for element in row[1:]:
                        # Check if the element is found in the search row
                        if element == search_row[0]:
                            row_numbers.append(row_num)
                            break

            # Store the row numbers as the value for the key in the dictionary
            result_dict[key] = row_numbers
            print(result_dict)

    # Print the dictionary with the data

    print('done!')
    # Print the dictionary with the data
    with open('my_dict.pkl', 'wb') as file:
        pickle.dump(result_dict, file)

    # try:
    #     for sublist in lists:
    #         if sublist[0] not in result_dict.keys():
    #             key = sublist[0]
    #             values = []
    #             with open(csv_file, 'r') as file:
    #                 reader = csv.reader(file)
    #                 for data in sublist[1:]:
    #                     row_number = None
    #                     for row_num, row in enumerate(reader, start=1):
    #                         if data in row:
    #                             row_number = row_num
    #                             break
    #                     values.append(row_number)
    #                     file.seek(0)  # Reset the file pointer to the beginning for the next search
    #             result_dict[key] = values
    #         else:
    #             break
    #
    #     print(result_dict)
    #     cpgGeneCSVTransfer3(result_dict)
    # except StopIteration:
    #     cpgGeneCSVTransfer3(result_dict)


def cpgGeneCSVTransfer3():
    input_file = 'C:/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv'
    output_data = []
    with open('my_dict.pkl', 'rb') as file:
        # Load the contents of the file using pickle
        data = pickle.load(file)

    # Now you can use the loaded data
    print(data)
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Skip rows until reaching the desired row number
        for key, value in data.items():
            output_file = f'C:/Users/npp8/PycharmProjects/pythonProject/Gene Grouping/{key}.csv'
            print("hey")
            # Iterate through each value in the list
            for i in range(0, len(value)):
                if i == 0:
                    count = 0
                    for _ in range(value[i]):
                        next(csv_reader)
                    row = next(csv_reader)
                    output_data.append(row)
                    count += 1
                    print("hey2")
                else:
                    diff = value[i] - value[i - 1] - count  # Subtract the current element from the preceding element
                    for _ in range(diff):
                        next(csv_reader)
                    row = next(csv_reader)
                    output_data.append(row)
                    print("hey3")
            # for row_number in value:
            #     for _ in range(row_number):
            #         next(csv_reader)
            #
            #     # Retrieve the row at the desired row number
            #     row = next(csv_reader)
            #     output_data.append(row)
            #     print("hey2")

            print("hey4")
            transposed_data = zip(*output_data)
            with open(output_file, 'w', newline='', encoding='UTF-8') as new_file:

                # Create a CSV writer object
                writer = csv.writer(new_file)
                # Write the selected rows to the new file
                writer.writerows(transposed_data)
                output_data = []
                print("done")
                file.seek(0)

def cpgGeneCreateCSVFile():
    import csv
    import os
    output_directory = 'C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping'  # Specify the output directory path
    with open('my_dict.pkl', 'rb') as file:
        # Load the contents of the file using pickle
        my_dict = pickle.load(file)

    for key in my_dict:
        file_name = os.path.join(output_directory, key + '.csv')
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write header or other required information if needed
            writer.writerow([])

def cpgGeneTransfer4():
    input_file = 'C:/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv'
    output_data = []
    final_dict = {}
    count = 0
    number = 50000
    with open('my_dict.pkl', 'rb') as file:
        # Load the contents of the file using pickle
        data = pickle.load(file)
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            count += 1
            for key, value in data.items():
                if count in value:
                    if key in final_dict:
                        final_dict[key].append(row)
                        print(count)
                        del row
                        break

                    else:
                        final_dict[key] = [row]
                        print(count)
                        del row
                        break
                if count == number:
                    if number == 50000:
                        with open('final_dict.pkl', 'wb') as file:
                            pickle.dump(final_dict, file)
                            final_dict = {}
                    #else:


    with open('final_dict.pkl', 'wb') as file:
        pickle.dump(final_dict, file)


def cpgGeneTransfer5():
    import os
    input_file = 'C:/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv'
    output_directory = 'C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping'
    output_data = []
    final_dict = {}
    count = 0
    with open('my_dict.pkl', 'rb') as file:
        # Load the contents of the file using pickle
        data = pickle.load(file)
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            count += 1
            for key, value in data.items():
                if count in value:
                    files = f'C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping/{key}.csv'
                    with open(files, 'a', newline='') as file2:
                        writer = csv.writer(file2)
                        writer.writerow(row)
def transpose():
    import os
    import csv

    directory = 'C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping'  # Path to the directory containing CSV files

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                rows = list(reader)

            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)

                for row in rows:
                    modified_row = [value if value != "NA" else "0" for value in row]
                    writer.writerow(modified_row)
        print(filename)
transpose()



