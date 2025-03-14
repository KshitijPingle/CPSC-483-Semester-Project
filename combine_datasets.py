# Kshtiij Pingle
import csv

# final_dataset.xlsx is the one to push everything into
# final_dataset  = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/final_dataset.xlsx"
final_dataset  = "../final_dataset.xlsx"
rows = []

# Go through each singlular file and get data
# file1 = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/country_life_expectancy_data_new.csv"
file1 = "../country_life_expectancy_data_new.csv"
with open(file1, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    counter = 0
    current_country = ""
    prev_country = ""
    for row in csvreader:
        # 'row' here is a dictionary
        if (counter == 0):
            # Append headers
            rows.append(row)
        else:
            current_country = row["Countries, territories and areas"]
            if (current_country == prev_country):
                # Skip
                continue
            # Otherwise append current row
            rows.append(row)
            # print(f"Added {current_country} to dataset")
            prev_country = current_country
        counter += 1

# file2 = "/mnt/c/Kshitij_Docs/Kshitij_CSUF/CPSC_483_Machine_Learning/Semester_Project/intermediate_csv_file_1.csv"
file2 = "intermediate_csv_file_1.csv"
with open(file2, 'w') as csvfile:
    fieldnames = ['Countries, territories and areas', 'Year', 'Life expectancy at birth (years), Both sexes', 'Life expectancy at birth (years), Male',
                  'Life expectancy at birth (years), Female', 'Life expectancy at age 60 (years), Both sexes', 'Life expectancy at age 60 (years), Male',
                  'Life expectancy at age 60 (years), Female', 'Healthy life expectancy (HALE) at birth (years), Both sexes', 'Healthy life expectancy (HALE) at birth (years), Male',
                  'Healthy life expectancy (HALE) at birth (years), Female', 'Healthy life expectancy (HALE) at age 60 (years), Both sexes',
                  'Healthy life expectancy (HALE) at age 60 (years), Male', 'Healthy life expectancy (HALE) at age 60 (years), Female']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    #write headers to file
    csvwriter.writeheader()

    # Now write every row to file
    csvwriter.writerows(rows)

# Now we have attached 1 file and 2,576 datapoints