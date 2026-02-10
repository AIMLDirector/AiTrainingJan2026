
from elasticsearch import Elasticsearch
from langchain.tools import tool

es = Elasticsearch("http://localhost:9200")

@tool
def fetch_critical_logs(index: str = "logs-*") -> str:
    """
    Return up to 10 CRITICAL logs.
    """
    query = {
        "size": 10,
        "query": {
            "match": {
                "severity": "CRITICAL"
            }
        },
        "sort": [{"@timestamp": {"order": "desc"}}]
    }

    res = es.search(index=index, body=query)
    hits = res["hits"]["hits"]
    if len(hits) == 0:
        return "NO_CRITICAL_ALERTS"

    formatted = []
    for h in hits:
        src = h["_source"]
        formatted.append(
            f"[{src.get('@timestamp')}] {src.get('service')} "
            f"{src.get('host')}: {src.get('message')}"
        )
    return "\n".join(formatted)