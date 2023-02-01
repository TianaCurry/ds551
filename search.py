# ds551 sp2023 hw01
# Question 3: search function
# By Tiana Curry

import sys
import requests
import pandas as pd

def data_retrieval(baseURL, startRange, endRange):
    '''Summary
       - This function will take the desired Firebase base url and create parameters for a query request
         to get a specified Avg AQI range with kyes as JSON string 
       - Three parameters
            - baseURL: desired Firebase base url from Realtime database
            - startRange: lower bound of the desired range
            - endRange: upper bound of the desired range
       - This script can be executed from the CLI execution format: python3 stat.py <arg 1> <arg 2> , arg 1,2= int
       - Prints a dataframe with columns(Country,Year,Month) with Avg AQI range[startRange,endRange]
    '''

    # create Firebase query parameters
    jsonParams =f'?orderBy="Avg AQI"&startAt={startRange}&endAt={endRange}&'
    #attach parameters to firebase database url for aqi.json
    completeURL = baseURL + jsonParams
    
    #pulling data results from our parameters
    resp = requests.get(completeURL)
    # outputs python dictionary
    asDict = resp.json()
    
    # dataframe from dictionary where index=rows and keys=columns
    queryDf = pd.DataFrame.from_dict(asDict, orient='index')
    # sort values in dataframe
    queryDf = queryDf.sort_values(by=["Country","Year","Month"])
    queryDf = queryDf.reset_index(drop=True)
    # create new dataframe with desired columns
    newQueryDf = queryDf[["Country","Year","Month"]].copy()
    
    with pd.option_context('display.max_rows', None,'display.max_columns', None):
        print(newQueryDf)

# executing function from CLI with multiple system arguments variables
if __name__ == '__main__':
    data_retrieval(*sys.argv[1:])   
          
