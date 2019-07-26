import os
from pymongo import MongoClient
import time
import pandas as pd
from from_jsons_to_classic_dataframe import *
import datetime as dt

# make conection with  database
client = MongoClient('172.25.5.233', 27017)
db = client['waze_bdt']
collection_waze = db['tt']

# get current time in ms
epoch_ms_now = int(round(time.time()*1000))

# write a query
myquery = { "updateTime": { "$lt": epoch_ms_now } } # every document with updatetime lesser than now.

# execute query, also time it
start = time.time()
mydocs = collection_waze.find(myquery)
print(time.time() - start, ' seconds of wall time to get query done.')   

df_tt, df_r = from_json_to_classic_df(mydocs)

# Check results
print(df_tt.head(3))
print(df_tt.tail(3))
print(df_tt.shape)

print(df_r.head(3))
print(df_r.tail(3))
print(df_r.shape)

# save to files
currentDT = dt.datetime.now()

df_tt.to_csv('./output/travel_times_' + currentDT.strftime("%Y_%m_%d_%H.%M.%S"))
df_r.to_csv('./output/routes' + currentDT.strftime("%Y_%m_%d_%H.%M.%S"))



# this is the "automatic" way, doesnt interprete well enought the files
# df = pd.DataFrame(list(mydocs))
# print(df.columns)

