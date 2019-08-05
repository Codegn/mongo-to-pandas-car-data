import json
import pandas as pd
from pathlib import Path
import datetime as dt
import pytz

def from_json_folder_to_json_docs(folder_path):
    """
    This was intended for local testing only
    to emulate a query result of mongodb
    """
    pathlist = Path(folder_path).glob('**/*.json')
    json_docs = []
    for path in pathlist:
        # because path is object not string
        path_in_str = str(path)
        with open(path_in_str) as f:
            json_docs.append(json.load(f))
    return json_docs

def from_json_to_classic_df(json_docs):
    # given a collection of json files
    list_of_travel_times = []
    dict_of_routes = {} # use a dict to not get duplicates

    for json_file in json_docs:
        
        if(str(json_file['updateTime'])[:-3]!=''):
            updateTime = dt.datetime.fromtimestamp(int(str(json_file['updateTime'])[:-3]), tz=pytz.timezone('America/Santiago'))
        else:
            pass

        for route in json_file['routes']:

            name = route['name']
            time = route['time']
            historicTime = route['historicTime']

            row_tt = [name, time, historicTime, updateTime]
            list_of_travel_times.append(row_tt)

            length = route['length']
            line = route['line']

            row_r = [name, length, line]
            dict_of_routes[name] = row_r

    list_of_routes = list(dict_of_routes.values())

    headers_tt = ['name', 'time', 'historictime', 'updatetime']
    df_tt = pd.DataFrame(list_of_travel_times, columns=headers_tt)

    headers_r = ['name', 'length', 'line']
    df_r = pd.DataFrame(list_of_routes, columns=headers_r)

    return df_tt, df_r



