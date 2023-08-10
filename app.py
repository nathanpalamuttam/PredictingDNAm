import shiny
from shiny import App, render, ui, reactive
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import pandas as pd
from scipy.stats import pearsonr




app_ui = ui.page_fluid(
    ui.panel_title("DNAm and Age Correlation"),

    ui.layout_sidebar(

        ui.panel_sidebar(
            ui.input_text("geneName", "Gene Name", placeholder="Enter text"),
            ui.input_select("in_select", "Select input",
                            ["", "Biological_Sex", "Cancer_Diagnosis_any", "Cardiovascular_any",
                             "High_Blood_Pressure", "High_Cholesterol", "Anemia", "Heart_Murmur",
                             "Heart_Attack",
                             "Stroke",
                             "Respiratory_Disease_any",
                             "Asthma",
                             "Chronic_Bronchitis",
                             "Cystic_Fibrosis",
                             "Pneumonia",
                             "Tuberculosis",
                             "Emphysema",
                             "COPD",
                             "Endocrine_Disease_any",
                             "Diabetes1",
                             "Diabetes2",
                             "Prediabetes",
                             "Osteoporosis",
                             "Skin_Hair_any",
                             "Gastrointestinal_any",
                             "Cirrhosis",
                             "Hepatitis",
                             "Genito_Urinary_any",
                             "Musculoskeletal_any",
                             "Gout",
                             "Rheumatoid_Arthritis",
                             "Neuropsychological_any",
                             "Alzheimer",
                             "Anxiety",
                             "Depression",
                             "Epilepsy",
                             "Migraines",
                             "Reproductive_any",
                             "Immune_any",
                             "Cytomegalovirus",
                             "Menopause",
                             "Recreational_Drug_Use_any",
                             "Amphetamines",
                             "Benzodiazepines",
                             "Marijuana",
                             "Hallucinogens",
                             "MDMA",
                             "Opioids",
                             "Drug_Alcohol_mother",
                             "Drug_Alcohol_father",
                             "Given_Birth",
                             "Telomere_Values",
                             "Metformin",
                             ]),
                ui.p(ui.input_action_button("Calculate", "Action button")),

        ),

        ui.panel_main(

            ui.output_table("negative"),
            ui.output_text("NegativeText"),
            ui.output_text("PositiveText"),
            ui.output_table("positive")
        ),
    ),
)


def server(input, output, session):
    @output
    @render.text
    @reactive.event(input.Calculate)
    def NegativeText():
        x = input.in_select()
        if x != "":
            return "This is when {} is 0".format(x)

    @output
    @render.text
    @reactive.event(input.Calculate)
    def PositiveText():
        x = input.in_select()
        if x != "":
            return "This is when {} is 1".format(x)
    @output
    @render.table
    @reactive.event(input.Calculate)
    def negative():
        #Join column from dem data and gene
        #Perform pearson correlation test
        conn = mysql.connector.connect(
            host="dnamagebackup.cqm0s5wdc0mz.us-east-2.rds.amazonaws.com",
            user="admin",
            password="dragon1234",
            database="dnamage",
            allow_local_infile=True
        )
        x = input.in_select()
        y = input.geneName()
        # Execute a query
        if x=="":
            query = "SELECT Age FROM DemData".format(x)
            query1 = "SELECT * FROM {}".format(y)
            df = pd.read_sql(query, con=conn)
            df2 = pd.read_sql(query1, con=conn)
            df2.replace(0, np.nan, inplace=True)
            result = pd.concat([df, df2], axis=1)
            x = result.iloc[:, 0]
            len()
            result_list = []
            # Iterate over the remaining columns
            for column in result.columns[1:]:
                # Select the current column as y
                y = result[column]

                # Exclude null values from x and y
                not_null_indices = pd.notnull(x) & pd.notnull(y)
                x_not_null = x[not_null_indices].astype(float)
                y_not_null = y[not_null_indices].astype(float)

                # Perform the Pearson correlation test
                correlation, p_value = pearsonr(x_not_null, y_not_null)
                result_list.append({'Column': column, 'Correlation': correlation, 'P-value': p_value})
                # Store the results in a dictionary
                resultValue = pd.DataFrame(result_list)
        else:
            query = "SELECT {}, Age FROM DemData".format(x)
            query1 = "SELECT * FROM {}".format(y)
            df = pd.read_sql(query, con=conn)
            df2 = pd.read_sql(query1, con=conn)
            df2.replace(0, np.nan, inplace=True)
            result = pd.concat([df, df2], axis=1)
            negative_value_table = result.loc[result[x] == 0]
            x = negative_value_table.iloc[:, 1]

            result_list = []
            # Iterate over the remaining columns
            for column in negative_value_table.columns[2:]:
                # Select the current column as y
                y = negative_value_table[column]

                # Exclude null values from x and y
                not_null_indices = pd.notnull(x) & pd.notnull(y)
                x_not_null = x[not_null_indices].astype(float)
                y_not_null = y[not_null_indices].astype(float)

                # Perform the Pearson correlation test
                correlation, p_value = pearsonr(x_not_null, y_not_null)
                result_list.append({'Column': column, 'Correlation': correlation, 'P-value': p_value})
                # Store the results in a dictionary
                resultValue = pd.DataFrame(result_list)

        # Print the results
        conn.close()
        return resultValue

    @output
    @render.table
    @reactive.event(input.Calculate)
    def positive():
        #Join column from dem data and gene
        #Perform pearson correlation test
        conn = mysql.connector.connect(
            host="dnamagebackup.cqm0s5wdc0mz.us-east-2.rds.amazonaws.com",
            user="admin",
            password="dragon1234",
            database="dnamage",
            allow_local_infile=True
        )
        y = input.geneName()
        x = input.in_select()
        if x != "":
        # Execute a query
            query = "SELECT {}, Age FROM DemData".format(x)
            query1 = "SELECT * FROM {}".format(y)
            df = pd.read_sql(query, con=conn)
            df2 = pd.read_sql(query1, con=conn)
            df2.replace(0, np.nan, inplace=True)
            result = pd.concat([df, df2], axis=1)
            positive_value_table = result.loc[result[x] == 1]
            x = positive_value_table.iloc[:, 1]

            result_list = []
            # Iterate over the remaining columns
            for column in positive_value_table.columns[2:]:
                # Select the current column as y
                y = positive_value_table[column]

                # Exclude null values from x and y
                not_null_indices = pd.notnull(x) & pd.notnull(y)
                x_not_null = x[not_null_indices].astype(float)
                y_not_null = y[not_null_indices].astype(float)

                # Perform the Pearson correlation test
                correlation, p_value = pearsonr(x_not_null, y_not_null)
                result_list.append({'Column': column, 'Correlation': correlation, 'P-value': p_value})
                # Store the results in a dictionary
                resultPositiveValue = pd.DataFrame(result_list)

        # Print the results
            conn.close()
            return resultPositiveValue


app = App(app_ui, server)
