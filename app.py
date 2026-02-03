import gradio as gr
from modules.paper_search import search_papers
from modules.pdf_downloader import download_papers
from modules.text_extractor import extract_text
from modules.analyzer import analyze_papers
from modules.draft_generator import generate_draft
from modules.reviewer import review_draft
from utils.helpers import save_output


def run_system(topic):
    try:
        # HARD RESET
        topic = topic.strip()
        if not topic:
            return "", "", "", "Please enter a research topic.", None

        # 1. Search top 3 paper
        papers = search_papers(topic)

        if not papers:
            return (
                "No papers found. Check internet or API key.",
                "",
                "",
                "Semantic Scholar returned no results.",
                None
            )

        # 2. Process pipeline
        pdfs = download_papers(papers)
        texts = extract_text(pdfs)
        analysis = analyze_papers(texts)
        draft = generate_draft(analysis)
        review = review_draft(draft)

        # 3. Save output
        file_path = save_output(draft)

        return (
            draft.get("Abstract", ""),
            draft.get("Methods", ""),
            draft.get("Results", ""),
            "\n".join(review) if isinstance(review, list) else str(review),
            file_path
        )

    except Exception as e:
        # FINAL SAFETY NET (prevents Gradio "Error")
        return (
            "System Error",
            "",
            "",
            f"Internal error: {str(e)}",
            None
        )
    
iface = gr.Interface(
    fn=run_system,
    inputs=gr.Textbox(label="Research Topic"),
    outputs=[
        gr.Textbox(label="Abstract"),
        gr.Textbox(label="Methods Comparison"),
        gr.Textbox(label="Results Synthesis"),
        gr.Textbox(label="Review Suggestions"),
        gr.File(label="Final Draft")
    ],
    title="AI System to Automatically Review and Summarize Research Papers"
)

if __name__ == "__main__":
    iface.launch()
