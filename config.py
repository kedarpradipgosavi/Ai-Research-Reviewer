import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_KEY")
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"

MAX_PAPERS = 4

DATA_DIR = "data"
PAPER_DIR = f"{DATA_DIR}/papers"
EXTRACTED_DIR = f"{DATA_DIR}/extracted"
OUTPUT_DIR = f"{DATA_DIR}/outputs"

