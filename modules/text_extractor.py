def extract_text(files):
    texts = []
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    texts.append(text)
        except Exception:
            continue
    return texts
