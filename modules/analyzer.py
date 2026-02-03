def analyze_papers(texts):
    # Simple aggregation (Semantic Scholar only)
    return [t for t in texts if isinstance(t, str) and t.strip()]
