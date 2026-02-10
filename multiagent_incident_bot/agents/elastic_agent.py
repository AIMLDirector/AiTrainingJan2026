
from langchain_core.tools import StructuredTool
from tools.elastic_tool import fetch_critical_logs

elastic_tool = StructuredTool.from_function(
    name="fetch_critical_logs",
    func=fetch_critical_logs,
    description="Fetch CRITICAL logs from Elasticsearch"
)