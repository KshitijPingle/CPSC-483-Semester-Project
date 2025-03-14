# Kshtiij Pingle
import csv
import os

# final_dataset.xlsx is the one to push everything into
# final_dataset  = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/final_dataset.xlsx"
final_dataset  = "../final_dataset.xlsx"
rows = []

# Go through each singlular file and get data
file1 = "../country_life_expectancy_data_new.csv"
with open(file1, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    current_country = ""
    prev_country = ""
    for row in csvreader:
        # 'row' here is a dictionary
        current_country = row["Countries, territories and areas"]
        if (current_country == prev_country):
            # Skip
            continue
        del row["Year"]
        # Otherwise append current row
        rows.append(row)
        # print(f"Added {current_country} to dataset")
        prev_country = current_country


def write_to_intermediate_file(rows, filename, fieldnames):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #write headers to file
        csvwriter.writeheader()
        # Now write every row to file
        csvwriter.writerows(rows)


fieldnames = ['Countries, territories and areas', 'Life expectancy at birth (years), Both sexes', 'Life expectancy at birth (years), Male',
              'Life expectancy at birth (years), Female', 'Life expectancy at age 60 (years), Both sexes', 'Life expectancy at age 60 (years), Male',
              'Life expectancy at age 60 (years), Female', 'Healthy life expectancy (HALE) at birth (years), Both sexes', 'Healthy life expectancy (HALE) at birth (years), Male',
              'Healthy life expectancy (HALE) at birth (years), Female', 'Healthy life expectancy (HALE) at age 60 (years), Both sexes',
              'Healthy life expectancy (HALE) at age 60 (years), Male', 'Healthy life expectancy (HALE) at age 60 (years), Female']
file2 = "intermediate_csv_file_1.csv"
write_to_intermediate_file(rows, file2, fieldnames)


# Now we have attached 1 file and 2,576 datapoints
# print(rows)
# Now process every file from data folder
directory_path = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/data"
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        # Process file
        # print(f"File: {filename}")
        with open(file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)

            counter = 0
            for row in csvreader:
                if (counter == 0):
                    # Skip headers
                    counter += 1
                    continue
                current_country = row["Country Name"]
                column_name = row["Series Name"]
                if (column_name not in fieldnames):
                    fieldnames.append(column_name)
                # print(f"Column name: {column_name}")
                # print(current_country)
                # Now find if we already have this country in rows
                country_found = False
                for row1 in rows:
                    country = row1["Countries, territories and areas"]
                    if (current_country == country):
                        # print(f"Found {current_country}")
                        country_found = True

                        # Check if we have a new column
                        if (column_name not in row1):
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
                counter += 1
    # break # For now

file3 = "intermediate_csv_file_2.csv"
write_to_intermediate_file(rows, file3, fieldnames)