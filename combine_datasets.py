# Kshtiij Pingle
import csv
import os

# Have code use country code instead of country names

# final_dataset.xlsx is the one to push everything into
# final_dataset  = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/final_dataset.xlsx"
final_dataset  = "../final_dataset.xlsx"
rows = []
fieldnames = []

# # Go through each singlular file and get data
# file1 = "../country_life_expectancy_data_new.csv"
# with open(file1, 'r') as csvfile:
#     csvreader = csv.DictReader(csvfile)
#     current_country = ""
#     prev_country = ""
#     for row in csvreader:
#         # 'row' here is a dictionary
#         current_country = row["Countries, territories and areas"]
#         if (current_country == prev_country):
#             # Skip
#             continue
#         del row["Year"]
#         # Otherwise append current row
#         rows.append(row)
#         # print(f"Added {current_country} to dataset")
#         prev_country = current_country


def write_to_intermediate_file(rows, filename, fieldnames):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #write headers to file
        csvwriter.writeheader()
        # Now write every row to file
        csvwriter.writerows(rows)


# fieldnames = ['Countries, territories and areas', 'Life expectancy at birth (years), Both sexes', 'Life expectancy at birth (years), Male',
#               'Life expectancy at birth (years), Female', 'Life expectancy at age 60 (years), Both sexes', 'Life expectancy at age 60 (years), Male',
#               'Life expectancy at age 60 (years), Female', 'Healthy life expectancy (HALE) at birth (years), Both sexes', 'Healthy life expectancy (HALE) at birth (years), Male',
#               'Healthy life expectancy (HALE) at birth (years), Female', 'Healthy life expectancy (HALE) at age 60 (years), Both sexes',
#               'Healthy life expectancy (HALE) at age 60 (years), Male', 'Healthy life expectancy (HALE) at age 60 (years), Female']
# file2 = "intermediate_csv_file_1.csv"
# write_to_intermediate_file(rows, file2, fieldnames)


# # Now we have attached 1 file and 2,576 datapoints
# # print(rows)
# # Now process every file from data folder
# directory_path = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/data"
# for filename in os.listdir(directory_path):
#     file_path = os.path.join(directory_path, filename)
#     if os.path.isfile(file_path):
#         # Process file
#         # print(f"File: {filename}")
#         with open(file_path, 'r') as csvfile:
#             csvreader = csv.DictReader(csvfile)

#             for row in csvreader:
#                 current_country = row["Country Name"]
#                 column_name = row["Series Name"]
#                 if (column_name not in fieldnames):
#                     fieldnames.append(column_name)
#                 # print(f"Column name: {column_name}")
#                 # print(current_country)
#                 # Now find if we already have this country in rows
#                 country_found = False
#                 for row1 in rows:
#                     country = row1["Countries, territories and areas"]
#                     if (current_country == country):
#                         # print(f"Found {current_country}")
#                         country_found = True

#                         # Check if we have a new column
#                         if (column_name not in row1):
#                             if (filename == "prevalence_of_overweight_adults_males_females.csv"):
#                                 # Complete data is from 2016
#                                 row1[column_name] = row["2016 [YR2016]"]
#                             elif (filename == "suicide_mortality_rate_total_females_males.csv"):
#                                 # Complete data is from 2019
#                                 row1[column_name] = row["2019 [YR2019]"]
#                             else:
#                                 # Else attach the latest one from 2020
#                                 row1[column_name] = row["2020 [YR2020]"]
#                         break
#     # break # For now

# file3 = "intermediate_csv_file_2.csv"
# write_to_intermediate_file(rows, file3, fieldnames)


# file4 = "../concentration_of_fine_particulate_matter_by_country.csv"
# with open(file4, 'r') as csvfile:
#     csvreader = csv.DictReader(csvfile)
#     country = ""
#     current_country = ""
#     # print(rows)

#     # for item in rows:
#     #     country = item["Countries, territories and areas"]
#     #     # print(f"Starting with {current_country}")
#     #     for row in csvreader:
#     #         indicator_name = row["Indicator"]
#     #         dim1 = row["Dim1"]
            
#     #         # Find all needed parameters for each country
#     #         key = ""
#     #         current_country =  row["Location"]
#     #         if (country == current_country):
#     #             # Insert new values
#     #             key = f"{indicator_name} in {dim1} Fact Value"
#     #             item[key] = row["FactValueNumeric"]

#     #             key = f"{indicator_name} in {dim1} Fact Value Low"
#     #             item[key] = row["FactValueNumericLow"]

#     #             key = f"{indicator_name} in {dim1} Fact Value High"
#     #             item[key] = row["FactValueNumericHigh"]
#     #         else:
#     #             # print(f"{current_country} != {current_country2}")
#     #             pass
#     for row in csvreader:
#         current_country = row["Location"]
#         indicator_name = row["Indicator"]
#         dim1 = row["Dim1"]

#         column_1 = f"{indicator_name} in {dim1} Fact Value"
#         column_2 = f"{indicator_name} in {dim1} Fact Value Low"
#         column_3 = f"{indicator_name} in {dim1} Fact Value High"

#         for item in rows:
#             country = item["Countries, territories and areas"]
#             if (current_country == country):
#                 # print(f"{current_country} == {country}")
#                 item[column_1] = row["FactValueNumeric"]
#                 item[column_2] = row["FactValueNumericLow"]
#                 item[column_3] = row["FactValueNumericHigh"]

            


# # Add required headers
# new_headers = ["Concentrations of fine particulate matter (PM2.5) in Cities Fact Value", "Concentrations of fine particulate matter (PM2.5) in Cities Fact Value Low",
#                "Concentrations of fine particulate matter (PM2.5) in Cities Fact Value High", "Concentrations of fine particulate matter (PM2.5) in Rural Fact Value",
#                "Concentrations of fine particulate matter (PM2.5) in Rural Fact Value Low", "Concentrations of fine particulate matter (PM2.5) in Rural Fact Value High",
#                "Concentrations of fine particulate matter (PM2.5) in Towns Fact Value", "Concentrations of fine particulate matter (PM2.5) in Towns Fact Value Low",
#                "Concentrations of fine particulate matter (PM2.5) in Towns Fact Value High", "Concentrations of fine particulate matter (PM2.5) in Urban Fact Value",
#                "Concentrations of fine particulate matter (PM2.5) in Urban Fact Value Low", "Concentrations of fine particulate matter (PM2.5) in Urban Fact Value High",
#                "Concentrations of fine particulate matter (PM2.5) in Total Fact Value", "Concentrations of fine particulate matter (PM2.5) in Total Fact Value Low", 
#                "Concentrations of fine particulate matter (PM2.5) in Total Fact Value High"]

# for item in new_headers:
#     fieldnames.append(item)

# # print(f"Fieldnames = :{fieldnames}:")
# file3 = "intermediate_csv_file_3.csv"
# write_to_intermediate_file(rows, file3, fieldnames)



# Start from fresh
rows = []
fieldnames = []

file1 = "../alcohol_consumption_per_capita_total_males_females.csv"
file1_copy = "../copy_of_alcohol_consumption_per_capita_total_males_females.csv"
country_count = 0
with open(file1, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if (country_count >= 217):
            break

        new_row = {}
        # print(row)
        country_name = row["Country Name"]
        country_code = row["Country Code"]
        new_row["Country Name"] = country_name
        new_row["Country Code"] = country_code
        if ("Country Name" not in fieldnames):
            fieldnames.append("Country Name")
        if("Country Code" not in fieldnames):
            fieldnames.append("Country Code")

        counter = 0
        with open(file1_copy, 'r') as copy_of_file1:
            csvreader2 = csv.DictReader(copy_of_file1)
            for row2 in csvreader2:
                current_code = row2["Country Code"]
                if (current_code == country_code):
                    if (counter == 3):
                        break
                    column_name = row2["Series Name"]
                    if (column_name not in fieldnames):
                        fieldnames.append(column_name)
                    new_row[column_name] = row2["2020 [YR2020]"]
                    counter += 1

        rows.append(new_row)
        country_count += 1

intermediate_file = "intermediate_csv_file_4.csv"
write_to_intermediate_file(rows, intermediate_file, fieldnames)
# 1 file completely attached, approx. 1090 datapoints added

# Now add everything from data folder
directory_path = "../data"
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    # print(file_path)
    if os.path.isfile(file_path):
        # Process this file
        with open(file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                country_code = row["Country Code"]
                column_name = row["Series Name"]
                if (column_name not in fieldnames):
                    fieldnames.append(column_name)
                
                # Now check if we have this country in rows
                for row1 in rows:
                    current_code = row1["Country Code"]
                    if (country_code == current_code):
                        if (filename == "prevalence_of_overweight_adults_males_females.csv"):
                            # Complete data is from 2016
                            row1[column_name] = row["2016 [YR2016]"]
                        elif (filename == "suicide_mortality_rate_total_females_males.csv"):
                            # Complete data is from 2019
                            row1[column_name] = row["2019 [YR2019]"]
                        else:
                            # Else attach the latest one from 2020
                            row1[column_name] = row["2020 [YR2020]"]
                        break

intermediate_file2 = "intermediate_csv_file_5.csv"
write_to_intermediate_file(rows, intermediate_file2, fieldnames)
# 18 files added now, approx. 5668 datapoints




file2 = "../concentration_of_fine_particulate_matter_by_country.csv"
with open(file2, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        country_code = row["SpatialDimValueCode"]
        indicator = row["Indicator"]
        residence_area_type = row["Dim1"]
        column_1 = f"{indicator} in {residence_area_type} Fact Value"
        column_2 = f"{indicator} in {residence_area_type} Fact Value Low"
        column_3 = f"{indicator} in {residence_area_type} Fact Value High"

        if (column_1 not in fieldnames):
            fieldnames.append(column_1)
        if (column_2 not in fieldnames):
            fieldnames.append(column_2)
        if (column_3 not in fieldnames):
            fieldnames.append(column_3)

        for row2 in rows:
            current_code = row2["Country Code"]
            if (current_code == country_code):
                # print(f"{current_country} == {country}")
                row2[column_1] = row["FactValueNumeric"]
                row2[column_2] = row["FactValueNumericLow"]
                row2[column_3] = row["FactValueNumericHigh"]


intermediate_file3 = "intermediate_csv_file_6.csv"
write_to_intermediate_file(rows, intermediate_file3, fieldnames)
# 19 files added now, approx 8578 datapoints


