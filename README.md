# AI Resume Screener

A web application that analyzes resumes against job descriptions using Llama 3, providing structured hiring intelligence across five dimensions.

Built with Python, Flask, and Groq API. Runs locally via Ollama or deployed via Groq.

---

## What it does

Upload a resume and paste a job description. The app runs five separate AI analyses and returns a structured report:

- **Fit Score** — overall candidate match out of 10, with strengths and missing skills
- **ATS Analysis** — keyword density, formatting issues, section completeness
- **Skill Gap Table** — side-by-side comparison of required vs present skills with gap severity
- **Interview Questions** — five targeted questions based on the candidate's weak areas
- **Career Roadmap** — personalized path suggestions with 3/6/12 month milestones and resources

Supports multi-resume comparison — upload up to two resumes against one job description and get a ranked table.

---

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| AI Model | Llama 3 (via Groq API / Ollama) |
| PDF Parsing | PyPDF |
| DOCX Parsing | python-docx |
| JD Scraping | BeautifulSoup, Requests |
| Storage | JSON (screening history) |
| Frontend | HTML, CSS, Vanilla JS |

---

## Features

- PDF and DOCX resume upload with drag-and-drop
- Job description URL scraper — paste a Naukri or Internshala link to auto-fill
- Multi-resume ranking with animated score bars
- Screening history with expand/collapse and download
- Table of contents with jump links on result page
- Copy and download individual or all reports
- Cycling loading messages during AI processing
- Fully dark UI, no external CSS frameworks

---

## Local setup

**Prerequisites:** Python 3.10+, Ollama (for local mode) or Groq API key (for cloud mode)

```bash
git clone https://github.com/Sam-Coder-DS/ai-resume-screener.git
cd ai-resume-screener
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

Run the app:

```bash
python app.py
```

Open `http://localhost:5000`

---

## Local mode with Ollama

To run without an API key using Ollama locally:

```bash
ollama pull llama3
```

Replace the Groq client in `screener.py` with:

```python
import ollama

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": prompt}]
)
return response["message"]["content"]
```

Note: set `CUDA_VISIBLE_DEVICES=""` if you encounter GPU errors on Windows.

---

## Project structure

```
resume_screener/
├── app.py              # Flask routes
├── screener.py         # AI analysis functions
├── prompt.py           # Prompt templates
├── scraper.py          # Job description scraper
├── requirements.txt
├── Procfile
└── templates/
    ├── index.html      # Upload form
    ├── result.html     # Analysis results
    └── history.html    # Past screenings
```

---

## Deployment

Deployed on Render. Environment variable `GROQ_API_KEY` set via Render dashboard.

Build command: `pip install -r requirements.txt`  
Start command: `python app.py`

---

