# Kshtiij Pingle
import csv
import os

# final_dataset.xlsx is the one to push everything into
final_dataset  = "../final_dataset.xlsx"
rows = []
fieldnames = []

def write_to_file(rows, filename, fieldnames):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #write headers to file
        csvwriter.writeheader()
        # Now write every row to file
        csvwriter.writerows(rows)


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

# intermediate_file = "intermediate_csv_file_1.csv"
# write_to_file(rows, intermediate_file, fieldnames)
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

# intermediate_file2 = "intermediate_csv_file_2.csv"
# write_to_file(rows, intermediate_file2, fieldnames)
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
                break


# intermediate_file3 = "intermediate_csv_file_3.csv"
# write_to_file(rows, intermediate_file3, fieldnames)
# 19 files added now, approx 8578 datapoints



file3 = "../gdp_of_countries.csv"
with open(file3, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    current_country = ""
    column_name = "GDP, current prices (Billions of U.S. dollars)"
    fieldnames += [column_name]

    for row in csvreader:
        current_country = row[column_name]
        for row2 in rows:
            country = row2["Country Name"]
            if (current_country == country):
                row2[column_name] = row["2023"]

# intermediate_file4 = "intermediate_csv_file_4.csv"
# write_to_file(rows, intermediate_file4, fieldnames)
# 20 files added, approx. 9,100 data points


file4 = "../happiness_data_with_country.csv"
with open(file4, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    current_country = ""
    country = ""
    column_1 = "Happiness Ladder Score"
    column_2 = "Happiness Ladder Score Upper Whisker"
    column_3 = "Happiness Ladder Score Lower Whisker"
    fieldnames += [column_1, column_2, column_3]

    for row in csvreader:
        current_country = row["Country name"]

        for row2 in rows:
            country = row2["Country Name"]
            if (current_country == country):
                row2[column_1] = row["Ladder score"]
                row2[column_2] = row["upperwhisker"]
                row2[column_3] = row["lowerwhisker"]
                break



file5 = "../share-of-population-that-cannot-afford-a-healthy-diet.csv"
with open(file5, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    prev_country = ""
    current_country = ""
    column_name = "Share of the population who cannot afford a healthy diet"
    fieldnames += [column_name]
    value = 0
    latest_year = 0

    for row in csvreader:
        current_country = row["Entity"]
        if (prev_country == current_country):
            year = row["Year"]
            if (year > latest_year):
                latest_year = year
                value = row[column_name]
        else:
            # Find the country in rows and add the value
            for row2 in rows:
                country = row2["Country Name"]
                if (prev_country == country):
                    row2[column_name] = value
                    break
            latest_year = row["Year"]
            value = row[column_name]
        prev_country = current_country
    
    # Find the country in rows and add the value
    for row2 in rows:
        country = row2["Country Name"]
        if (current_country == country):
            row2[column_name] = value
            break
# 22 files added



file6 = "../pop_density.csv"
with open(file6, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    current_code = ""
    column_name = "Population density (people per sq. km of land area)"
    fieldnames += [column_name]

    for row in csvreader:
        current_code = row["Country Code"]
        value = row["2022"]
        if (value == ""):
            value = row["2021"]
        
        # Add the value to rows
        for row2 in rows:
            country_code = row2["Country Code"]
            if (current_code == country_code):
                row2[column_name] = value
                break


# Add life expectancy data (The Target Labels)
file7 = "../country_life_expectancy_data_new.csv"
with open(file7, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    current_country = ""
    prev_country = ""

    for row in csvreader:
        current_country = row["Countries, territories and areas"]
        if (current_country == [prev_country]):
            continue
        
        # Now find that country in rows and add
        for row2 in rows:
            country = row2["Country Name"]
            if (current_country == country):
                row2["Life expectancy at birth (years), Both sexes"] = row["Life expectancy at birth (years), Both sexes"]
                row2["Life expectancy at birth (years), Male"] = row["Life expectancy at birth (years), Male"]
                row2["Life expectancy at birth (years), Female"] = row["Life expectancy at birth (years), Female"]
                row2["Life expectancy at age 60 (years), Both sexes"] = row["Life expectancy at age 60 (years), Both sexes"]
                row2["Life expectancy at age 60 (years), Male"] = row["Life expectancy at age 60 (years), Male"]
                row2["Life expectancy at age 60 (years), Female"] = row["Life expectancy at age 60 (years), Female"]
                row2["Healthy life expectancy (HALE) at birth (years), Both sexes"] = row["Healthy life expectancy (HALE) at birth (years), Both sexes"]
                row2["Healthy life expectancy (HALE) at birth (years), Male"] = row["Healthy life expectancy (HALE) at birth (years), Male"]
                row2["Healthy life expectancy (HALE) at birth (years), Female"] = row["Healthy life expectancy (HALE) at birth (years), Female"]
                row2["Healthy life expectancy (HALE) at age 60 (years), Both sexes"] = row["Healthy life expectancy (HALE) at age 60 (years), Both sexes"]
                row2["Healthy life expectancy (HALE) at age 60 (years), Male"] = row["Healthy life expectancy (HALE) at age 60 (years), Male"]
                row2["Healthy life expectancy (HALE) at age 60 (years), Female"] = row["Healthy life expectancy (HALE) at age 60 (years), Female"]

        prev_country = current_country

fieldnames += ["Life expectancy at birth (years), Both sexes", "Life expectancy at birth (years), Male",
               "Life expectancy at birth (years), Female", "Life expectancy at age 60 (years), Both sexes",
               "Life expectancy at age 60 (years), Male", "Life expectancy at age 60 (years), Female", 
               "Healthy life expectancy (HALE) at birth (years), Both sexes", "Healthy life expectancy (HALE) at birth (years), Male", 
               "Healthy life expectancy (HALE) at birth (years), Female", "Healthy life expectancy (HALE) at age 60 (years), Both sexes", 
               "Healthy life expectancy (HALE) at age 60 (years), Male", "Healthy life expectancy (HALE) at age 60 (years), Female"]

intermediate_file5 = "intermediate_csv_file_5.csv"
write_to_file(rows, intermediate_file5, fieldnames)
# 24 files added, approx. 12,700 datapoints right now





