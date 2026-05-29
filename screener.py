import pypdf
import io
import docx
from prompt import build_prompt, build_interview_prompt, build_ats_prompt, build_skill_gap_prompt, build_career_roadmap_prompt
from dotenv import load_dotenv
import os
load_dotenv()
from groq import Groq
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
def extract_text(file):
    reader = pypdf.PdfReader(io.BytesIO(file.read()))
    return " ".join([page.extract_text() for page in reader.pages])
def extract_text_docx(file):     
    document = docx.Document(io.BytesIO(file.read()))
    return " ".join([para.text for para in document.paragraphs])
def screen_resume(resume_text, job_desc):
    prompt = build_prompt(resume_text, job_desc)
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
def generate_interview_questions(resume_text, job_desc):
    prompt=build_interview_prompt(resume_text, job_desc)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
def generate_ats_score(resume_text):
    prompt=build_ats_prompt(resume_text)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
def generate_skill_gap(resume_text, job_desc):
    prompt=build_skill_gap_prompt(resume_text, job_desc)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
def generate_career_roadmap(resume_text):
    prompt=build_career_roadmap_prompt(resume_text)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content