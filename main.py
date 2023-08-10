import csv
import pandas as pd


def putDataIntoMySQL():
    folder_path = "C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping"
    lister = []  # Replace with the path to your folder
    # Iterate through the files in the folder

    for filename in os.listdir(folder_path):
        querycommands = []
        conn = mysql.connector.connect(
            host="dnam-age-correlation.cqm0s5wdc0mz.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database="dnamage",
            allow_local_infile=True
        )
        cursor = conn.cursor()
        if filename.endswith(".csv"):
            # Check if the file is a CSV file
            file_path = os.path.join(folder_path, filename)
            geneName = filename[:-4]
            # Process the CSV file
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                lister = next(reader)
                for i in range(0, len(lister)):
                    if i == 0:
                        create_table_query = f"""
                                        CREATE TABLE {geneName} (
                                            {lister[0]} DOUBLE
                                        )
                                        """
                        querycommands.append(create_table_query)
                    else:
                        alter_table_query = f"ALTER TABLE {geneName} ADD COLUMN {lister[i]} DOUBLE"
                        querycommands.append(alter_table_query)


                for command in querycommands:
                    cursor.execute(command)
                    cursor.fetchall()
                    cursor.close()
                    cursor = conn.cursor()
                conn.commit()
                cursor = conn.cursor(buffered=True)


                upload_data_query = f"LOAD DATA LOCAL INFILE 'C://Users/npp8/Desktop/GeneGroupings/{geneName}.csv' INTO TABLE {geneName} FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"
                cursor.execute(upload_data_query)
                conn.commit()
                print(geneName)
                conn.close()
                cursor.close()
def write_new_csv():
    # Specify the path to the input CSV file
    input_file = '/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv'

    # Specify the number of rows per output file
    rows_per_file = 5000

    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Skip the header row if present


        # Initialize variables
        current_row = 0
        current_file = 1
        output_file = f'output_{current_file}.csv'
        output_data = []
        next(reader, None)

        # Read the file in chunks
        for row in reader:
            # Add the row to the output data

            output_data.append(row)
            current_row += 1

            # If the desired number of rows is reached, write to the output file
            if current_row == rows_per_file:
                with open(output_file, 'w', newline='') as output:
                    writer = csv.writer(output)

                    # Write the header if present


                    # Write the data rows
                    writer.writerows(output_data)

                # Increment the file number and reset variables for the next chunk
                current_file += 1
                output_file = f'output_{current_file}.csv'
                output_data = []
                current_row = 0

        # Write the remaining data to the last output file
        if output_data:
            with open(output_file, 'w', newline='') as output:
                writer = csv.writer(output)

                # Write the header if present


                # Write the remaining data rows
                writer.writerows(output_data)

def writeFromOriginalFile():


    old_file_path = 'C:/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv'
    new_file_path = 'C:/Users/npp8/Desktop/File Extraction/FirstHundredRows.csv'

    # Open the old CSV file for reading
    with open(old_file_path, 'r') as old_file:
        # Create a CSV reader object
        reader = csv.reader(old_file)

        # Read the first 10 rows from the reader
        rows = [next(reader) for _ in range(100)]

    # Open the new CSV file for writing
    with open(new_file_path, 'w', newline='') as new_file:
        # Create a CSV writer object
        writer = csv.writer(new_file)

        # Write the selected rows to the new file
        writer.writerows(rows)

def storeCpGbyGene():
    filepath = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneCpG.csv'
    directory = 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/'

    with open(filepath, 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        next(reader)
        listOfGenes = []

        count = 0
        # Iterate over each row in the file
        for row in reader:
            if row[1] not in listOfGenes:
                listOfGenes.append(row[1])
                newList = []
                newList.append(row[1])
                with open(filepath, 'r') as file_inner:
                #     output_file = f'{row[1]}.csv'
                #     output_data = []
                    reader_inner = csv.reader(file_inner)
                    for newrow in reader_inner:
                        if newrow[1] == row[1]:
                            newList.append(newrow[0])

                    lists.append(newList)
                    #         output_data.append(newrow)
                    # with open(output_file, 'w', newline='') as output:
                    #     writer = csv.writer(output)
                    #
                    #     # Write the data rows
                    #     writer.writerows(output_data)



            # Process each row as needed
def getCpGFromLargeDataset():
    lists =[['RBL2', 'cg07881041', "cg13871826", 'cg00000029', 'cg00011284', 'cg01016459', 'cg01783195', 'cg01873277', 'cg02021817', 'cg02119764', 'cg02851944', 'cg03943270', 'cg04767752', 'cg06393130', 'cg07396495', 'cg07886896', 'cg09147843', 'cg09717219', 'cg11076723', 'cg11949307', 'cg12190057', 'cg12360270', 'cg12823025', 'cg13426503', 'cg15216023', 'cg17002920', 'cg17331051', 'cg18163803', 'cg18381420', 'cg21935094', 'cg22562509', 'cg26589132', 'cg26932830']]
    # Path to the input CSV file
    input_file = 'C:/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv'
    # Open input and output files
    with open(input_file, "r", newline="") as file_in:
        # Iterate through rows in the input file
        reader = csv.reader(file_in)
        for row in reader:
            for sublist in lists:
                output_file = f'{sublist[0]}.csv'
                output_data = []
                for item in sublist:
                     # Input string to match
                    target_string = item.strip()
                    # Check if the first column matches the target string
                    if row[0] == target_string:
                        # Write the matching row to the output file
                        output_data.append(row)
                transposed_data = zip(*output_data)

            with open(output_file, 'w', newline='') as new_file:

                        # Create a CSV writer object
                        writer = csv.writer(new_file)
                        # Write the selected rows to the new file
                        writer.writerows(transposed_data)
def getCpGFromLargeDatasetPandas():
    lists =[['RBL2', 'cg07881041', "cg13871826",
'cg00000029', 'cg00011284', 'cg01016459', 'cg01783195', 'cg01873277', 'cg02021817', 'cg02119764', 'cg02851944', 'cg03943270', 'cg04767752', 'cg06393130', 'cg07396495', 'cg07886896', 'cg09147843', 'cg09717219', 'cg11076723', 'cg11949307', 'cg12190057', 'cg12360270', 'cg12823025', 'cg13426503', 'cg15216023', 'cg17002920', 'cg17331051', 'cg18163803', 'cg18381420', 'cg21935094', 'cg22562509', 'cg26589132', 'cg26932830']]
    # Path to the input CSV file


    # Read the CSV file into a DataFrame
    df = pd.read_csv('C:/Users/npp8/Desktop/File Extraction/Normalized.Beta.12k.csv')
    pass
    column_name = ''
    for sublist in lists:
        output_file = f'{sublist[0]}.csv'
        output_data = []
        for item in sublist:
    # Search for a specific value in a column
            search_value = item
            matching_rows = []
            for index, row in df.iterrows():
                if row[column_name] == search_value:
                    matching_rows.append(row)
    # Create an empty list to store matching rows


    # Iterate over the DataFrame and append matching rows to the list


    # Print the matching rows
    for row in matching_rows:
        print(row)


def remove_duplicates():
    # Read the input CSV file into a pandas DataFrame
    df = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Gene and CpG.csv')

    df['UCSC_RefGene_Name'] = df['UCSC_RefGene_Name'].astype(str)
    df = df[df['UCSC_RefGene_Name'] != 'nan']
    # Remove duplicate values in the 'UCSC_RefGene_Name' column
    df['UCSC_RefGene_Name'] = df['UCSC_RefGene_Name'].apply(lambda x: ';'.join(sorted(set(x.split(';')))))

    # Write the modified DataFrame to a CSV file
    df.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/GeneCpG.csv', index=False)
# Usage example
putDataIntoMySQL()



