import os

PAPER_DIR = "data/papers"
os.makedirs(PAPER_DIR, exist_ok=True)

def download_papers(papers):
    files = []

    for i, paper in enumerate(papers):
        path = os.path.join(PAPER_DIR, f"paper_{i}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(paper.get("abstract") or "")
        files.append(path)

    return files
