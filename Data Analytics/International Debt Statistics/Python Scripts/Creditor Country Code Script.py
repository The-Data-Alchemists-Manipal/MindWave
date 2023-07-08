#Import required packages
import pandas as pd
import json
import requests

#Get all data sources from World Bank website
sources = requests.get("http://api.worldbank.org/v2/sources?per_page=100&format=json")
sourcesJSON = sources.json()

#Get ID of required data source
for i in sourcesJSON[1]:
    if i["name"] == "International Debt Statistics":
        print("ID of International Debt Statistics is " + i["id"])
    else:
        pass

#Get indicator code of required data
indicators = requests.get("http://api.worldbank.org/v2/indicator?format=json&source=6&per_page=600")
indicatorsJSON = indicators.json()
for i in indicatorsJSON[1]:
    IDSindicators = (i["id"],i["name"])
    print(i['id'], i['name'])

#Getting information of selected indicator
indicator = "DT.DOD.BLAT.CD"
for dict_entity in indicatorsJSON[1]:
    if dict_entity["id"] == indicator:
        print(dict_entity["sourceNote"])
    else:
        pass

# Requesting the locations
clocations = requests.get("http://api.worldbank.org/v2/sources/6/counterpart-area?per_page=300&format=JSON")
clocationsJSON = clocations.json()

# Parse through the response to see the location IDs and names
clocations = clocationsJSON["source"][0]["concept"][0]["variable"]
listLen = int(len(clocations))

# Create dataframe with location values
df = pd.DataFrame(columns=["id", "value"])     
for i in range(0,listLen):
    code = clocations[i]["id"]
    name = clocations[i]["value"]
    df = df.append({"id":code, "value":name}, ignore_index = True)
clocationsList = df
print(clocationsList)

#Converting the gathered data into Excel file
clocationsList.to_excel('Creditor Country Code.xlsx')
print("Excel File Saved")