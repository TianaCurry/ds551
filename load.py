# ds551 sp2023 hw01
# Question 2: load function
# By Tiana Curry

import sys
import json
import requests

def database_upload(jsonFile, firebaseURL):
    '''Summary
       - This function will take in data as a JSON file and import the data into a Firebase Realtime database
       - Two parameters
            - jsonFile: a json file with extention <file name>.json
            - FirebaseURL: location of the desired Realtime database with json file in the format of <database-url>/aqi.json 
       - This script can be executed from the CLI using: python3 load.py aqi.json <database-url>/aqi.json
       - Return None and updates Firebase Realtime database
    '''
    
    with open(jsonFile, 'r') as outfile:
        jsonData = json.load(outfile)
    
    requests.put(url= firebaseURL, json= jsonData)

# executing function from CLI with multiple system arguments variables
if __name__ == '__main__':
    database_upload(*sys.argv[1:])    
