### Run the following instructions:

docker run --rm -it --name query_mongo -v ${PWD}:/usr/src/code -w /usr/src/code --network="host" python:3 /bin/bash

pip install -r requirements.txt

python query_df_tt_and_df_r.py

### It will save in an output folder two csv files with travel times and routes.
