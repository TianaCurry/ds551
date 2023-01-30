# ds551 sp2023 hw01
# function for question 1
# Tiana Curry

import sys
import pandas as pd
import json

def aqi_average(aqicsv,aqijson):
    """Summary
       This function caluates the month averge per year for each country list in the csv file.
       And outputs as a JSON file.
       This program takes the follow parameters:
            - input: an csv file format <file name>.csv
            - output: name of the json file format <file name>.json
       You can run this program from the CLI using: "python3 stat.py <arg 1> <arg 2>"
    """
    # creating desired column in raw dataset
    aqi_df = pd.read_csv(str(aqicsv))
    aqi_df[["Year","Month","Day"]]= aqi_df["Date"].str.split("-", expand=True)
    
    # creating df with AQI monthly average by country and year
    aqi_avg = aqi_df.groupby(["Country","Year","Month"]).mean(numeric_only=True)
    
    aqi_avg = aqi_avg.rename(columns={"AQI Value":"Avg AQI"}).reset_index()
    aqi_avg["Year"] = aqi_avg["Year"].astype("int64")
    aqi_avg["Month"] = aqi_avg["Month"].astype("int64")
    #changing 3 numeric columns to the desire format
    
    aqi_avg["Avg AQI"] = aqi_avg["Avg AQI"].round(1)
    # convert df to dict to json str
    aqi_dict = aqi_avg.to_dict(orient= "records")
    aqi_json = json.dumps(aqi_dict)
    # creating json file
    with open(str(aqijson), 'w') as outfile:
        outfile.write(aqi_json)

# executing in CLI with multiple system arguments variables
if __name__ == '__main__':
    # takes at least two system arguments from CLI
    aqi_average(*sys.argv[1:])

