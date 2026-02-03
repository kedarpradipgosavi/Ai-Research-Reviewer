import os
import requests

SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"
API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

def search_papers(topic):
    headers = {
        "User-Agent": "AI-Research-Reviewer",
        "x-api-key": API_KEY
    }

    params = {
        "query": topic.strip(),
        "limit": 3,
        "fields": "title,authors,year,abstract,url"
    }

    try:
        response = requests.get(
            SEMANTIC_SCHOLAR_API,
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json().get("data", [])[:3]

    except Exception as e:
        print("Semantic Scholar Error:", e)
        return []
