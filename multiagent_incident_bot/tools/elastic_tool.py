import requests
import os
from dotenv import load_dotenv
load_dotenv()

def fetch_critical_logs():
    url = f"{os.getenv('ELASTIC_URL')}/{os.getenv('ELASTIC_INDEX')}/_search"

    query = {
        "size": 5,
        "query": {
            "bool": {
                "must": [
                    {"match": {"level": "CRITICAL"}},
                    {"range": {"@timestamp": {"gte": "now-45m"}}}
                ]
            }
        }
    }

    response = requests.post(url, json=query)
    response.raise_for_status()

    hits = response.json()["hits"]["hits"]
    #print(hits)
    return [hit["_source"] for hit in hits]

#fetch_critical_logs()