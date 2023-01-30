# write Python script that computes the average AQI value of each country from July 2022 to January 2023
# Output the results in a JSON file in the following format
# [{“Country”: “Albania”, “Year”: 2022, “Month”: 7, “Avg AQI”: 32.9}, …] 
# input file: aqi.csv
# output file: aqi.json
import sys
import pandas
import requests
import json
