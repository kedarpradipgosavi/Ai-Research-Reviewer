import os
import pandas as pd

OUTPUT_DIR = "data/outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_output(draft):
    path = os.path.join(OUTPUT_DIR, "final_draft.txt")
    with open(path, "w", encoding="utf-8") as f:
        for section, content in draft.items():
            f.write(section + "\n")
            f.write("-" * 40 + "\n")
            f.write((content or "No content generated.") + "\n\n")
    return path


def save_papers_excel(papers, topic):
    rows = []
    for p in papers[:3]:
        rows.append({
            "Title": p.get("title"),
            "Year": p.get("year"),
            "Authors": ", ".join(a["name"] for a in p.get("authors", [])),
            "URL": p.get("url"),
            "Abstract": p.get("abstract")
        })

    df = pd.DataFrame(rows)
    path = os.path.join(
        OUTPUT_DIR,
        f"{topic.replace(' ', '_')}_top_3_papers.xlsx"
    )
    df.to_excel(path, index=False)
    return path


