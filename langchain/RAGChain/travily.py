from tavily import TavilyClient

tavily_client = TavilyClient(api_key="")
response = tavily_client.search("Who is Leo Messi?")

print(response)