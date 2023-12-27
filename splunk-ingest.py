# data.csv has following records
# id,amount,action,location,is_fraud
# 290,8978,transfer,New York,False
# this script convert csv to json and post to splunk
# {"event": {"id": 290, "amount": 8978, "action": "transfer", "location": "New York", "is_fraud": False}, "sourcetype": "_json"}

import pandas as pd
import json

df = pd.read_csv("timeseries_data.csv")
json_records = df.to_json(orient='records')
json_records = json.loads(json_records)
for record in json_records:
    print(json.dumps({"event": record, "sourcetype": "_json"}))

# Post these records to splunk via REST API
import requests
import time
for record in json_records:
    response = requests.post("http://8698ce922ce5.ngrok.app/services/collector/event", headers={"Authorization": "Splunk bf965e21-aa24-4595-803f-f2270bd7e45c"}, data=json.dumps({"event": record, "sourcetype": "_json","index":"main"}))
    # sleep for 5 seconds

    time.sleep(5)
    print(response.status_code)
