## Run the following instructions:

Create a ephimeral container to query mongo:
1. docker run --rm -it --name eph_query_mongo -v ${PWD}:/usr/src/code -w /usr/src/code --network="host" python:3 /bin/bash
2. pip install -r requirements.txt
3. use a query file

Create a persistent container to query mongo:
1. docker run -it --name query_mongo -v ${PWD}:/usr/src/code -w /usr/src/code --network="host" python:3 /bin/bash
2. pip install -r requirements.txt (once)
3. use a query file
4. restar container with: docker start query_mongo -ai

If you want to use conda:
1. conda create -n query_mongo pymongo=3.8.0 pandas pytz
2. conda activate query_mongo

Query files:
1. python query_df_tt_and_df_r.py
2. python query_df_tt_and_df_r_between_dates.py (modify dates inside)

### It will save in an output folder two csv files with travel times and routes.
