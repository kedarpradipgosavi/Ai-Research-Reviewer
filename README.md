# AI Research Reviewer

An end to end AI system that automatically retrieves, analyzes, summarizes, and generates structured review drafts from research papers.

Developed as part of the Infosys Internship Program.

---

## Overview

This system automates literature review by:

- Retrieving research papers using Semantic Scholar API
- Downloading and extracting text from PDFs
- Normalizing and cleaning extracted content
- Performing LLM based semantic sectioning
- Conducting cross paper analysis
- Generating structured review drafts
- Displaying results using a Gradio interface

---

## Project Structure

Ai-Research-Reviewer/
│
├── Documents/
├── data/
├── modules/
│   ├── paper_search.py
│   ├── pdf_downloader.py
│   ├── text_extractor.py
│   ├── analyzer.py
│   ├── draft_generator.py
│   ├── reviewer.py
│
├── utils/
├── app.py
├── config.py
└── requirements.txt

---

## Tech Stack

- Python
- Semantic Scholar API
- PyMuPDF
- Google Gemini API
- Gradio

---

Create virtual environment:

python -m venv venv  
venv\Scripts\activate  

Install dependencies:

pip install -r requirements.txt

---

## Run the Application

python app.py

Open the generated local link to access the Gradio UI.

---

## Key Features

- Automated research paper retrieval
- PDF text extraction and normalization
- LLM based section detection
- Cross paper comparative analysis
- Structured review generation
- Interactive UI

---

## Author

Kedar Pradip Gosavi  
Infosys Internship Project
