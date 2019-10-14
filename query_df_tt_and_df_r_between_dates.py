import os
from from_jsons_to_classic_dataframe import *
from pymongo import MongoClient
import time
import pandas as pd
import datetime as dt
from time import strptime, strftime, mktime, gmtime
import re

def convert_timezone_to_utc_epoch(timestamp_string, timezone):

    local_tz = pytz.timezone(timezone)
    ts = dt.datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S')
    ts = local_tz.localize(ts)
    ts = str(ts.astimezone(pytz.utc))[0:19]
    epoch = int(time.mktime(time.strptime(ts, '%Y-%m-%d %H:%M:%S')))
    return epoch*1000 #in ms

def query_between_times(str_date_i, str_date_f):

    # use function to transform from local time to 
    epoch_date_i = convert_timezone_to_utc_epoch(str_date_i, 'America/Santiago')
    epoch_date_f = convert_timezone_to_utc_epoch(str_date_f, 'America/Santiago')

    # write a query
    myquery = { "$and": [ { "updateTime": { "$gte": epoch_date_i } }, { "updateTime": { "$lt": epoch_date_f } } ] } # every document with updatetime lesser than now.

    # make conection with  database
    client = MongoClient('172.25.5.233', 27017)
    db = client['waze_bdt']
    collection_waze = db['tt']

    mydocs = collection_waze.find(myquery)  

    df_tt, df_r = from_json_to_classic_df(mydocs)

    # Check results
    print(df_tt.head(3))
    print(df_tt.tail(3))
    print(df_tt.shape)

    print(df_r.head(3))
    print(df_r.tail(3))
    print(df_r.shape)

    # save to files
    df_tt.to_csv('./output/travel_times_' + 'from_' + re.sub('[^0-9]','', str_date_i) + '_to_' + re.sub('[^0-9]','', str_date_f) + '.csv')
    df_r.to_csv('./output/routes_' + 'from_' + re.sub('[^0-9]','', str_date_i) + '_to_' + re.sub('[^0-9]','', str_date_f) + '.csv')

if __name__ == "__main__":
    query_between_times('2019-09-23 00:00:00','2019-10-10 00:00:00')
