import os
import csv
import mysql.connector
import subprocess


def findAndReplace():
    folder_path = "C://Users/npp8/Desktop/GeneGroupings"  # Replace with the path to your folder
    find_value = "NA"  # Replace with the value you want to find
    replace_value = "0"
    # Iterate through the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):  # Check if the file is a CSV file
            file_path = os.path.join(folder_path, filename)  # Get the full file path
            # Process the CSV file
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                # Perform operations on the CSV file, such as reading or parsing the data
                # Example: Read the contents of the CSV file
                rows = list(reader)  # Read all rows into memory as a list

                # Iterate over each row and replace the value
                for row in rows:
                    for i, cell in enumerate(row):
                        if cell == find_value:
                            row[i] = replace_value

                # Write the modified data back to the original CSV file
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                print("Value replaced in " + file_path)
                # Additional processing logic can be applied here

def GeneNameExcel():
    import os
    import csv

    # Path to the folder containing CSV files
    folder_path = "C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping"

    # List all files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

    # Create a new CSV file and write all the CSV file names
    output_csv_path = os.path.join("C://Users/npp8/PycharmProjects/pythonProject", "all_csv_names.csv")
    with open(output_csv_path, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerow(["CSV File Names"])  # Write header

        for csv_file in csv_files:
            csv_writer.writerow([csv_file])

    print("All CSV file names saved to a single CSV file.")


def putDataIntoMySQL():
    folder_path = "C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping"
    lister = []  # Replace with the path to your folder
    # Iterate through the files in the folder CELSR2 CXCR2P1_RUFY4 CXorf48 GAGE12B_GAGE12C_GAGE12D_GAGE12E_GAGE12G_GAGE12H_GAGE2A_GAGE2E_GAGE8 = GAGE12B___
    # GAGE12C_GAGE12D_GAGE12E_GAGE12G_GAGE6 = GAGE12C___
    # GAGE12F_GAGE12I_GAGE2A_GAGE2C_GAGE2D_GAGE2E_GAGE4_GAGE5_GAGE7_GAGE8 = GAGE12F___
    # GAGE12I_GAGE2A_GAGE2C_GAGE2D_GAGE2E_GAGE4_GAGE5_GAGE7_GAGE8 = GAGE12I___

    startfile = '1_Dec.csv'
    start_index = os.listdir(folder_path).index(startfile)
    for filename in os.listdir(folder_path)[start_index:]:
            querycommands = []
            conn = mysql.connector.connect(
                host="dnamagebackup.cqm0s5wdc0mz.us-east-2.rds.amazonaws.com",
                user="admin",
                password="dragon1234",
                database="dnamage",
                allow_local_infile=True
            )
            cursor = conn.cursor()
            if filename.endswith(".csv"):
                # Check if the file is a CSV file
                file_path = os.path.join(folder_path, filename)
                geneName = filename[:-4]
                # Process the CSV file
                if filename.startswith("1"):
                    geneNameTemp = geneName
                    geneName = "_" + geneName
                    upload_data_query = f"LOAD DATA LOCAL INFILE 'C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping/{geneNameTemp}.csv' INTO TABLE {geneName} FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"
                else:
                    upload_data_query = f"LOAD DATA LOCAL INFILE 'C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping/{geneName}.csv' INTO TABLE {geneName} FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES"
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



                    cursor.execute(upload_data_query)
                    conn.commit()
                    print(geneName)
                    conn.close()
                    cursor.close()


def changeFileNames():
    folder_path = "C://Users/npp8/PycharmProjects/pythonProject/Gene Grouping"
    for filename in os.listdir(folder_path):
        if filename.endswith('_csv'):
            print(1)# Process only CSV files
            file_path = os.path.join(folder_path, filename)
            new_filename = filename[:-4] + '.' + filename[-3:]
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)


GeneNameExcel()
