import json
from datetime import datetime
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
from flask import Flask, render_template, request
from screener import extract_text, screen_resume, extract_text_docx, generate_interview_questions, generate_ats_score, generate_skill_gap, generate_career_roadmap
from scraper import scrape_job_description
def save_history(filename, result):
    try:
        with open("history.json", "r") as f:
            history = json.load(f)
    except:
        history = []
    
    history.append({
        "filename": filename,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    
    with open("history.json", "w") as f:
        json.dump(history, f)
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/history")
def history():
    try:
        with open("history.json", "r") as f:
            data = json.load(f)
    except:
        data = []
    return render_template("history.html", history=data)  
@app.route("/clear_history", methods=["POST"])
def clear_history():
    with open("history.json", "w") as f:
        json.dump([], f)
    return "ok"
@app.route("/screen", methods=["POST"])
def screen():
    resume_files=request.files.getlist("resumes")
    if len(resume_files) > 2:
        return "Maximum 2 resumes allowed at once.", 400
    job_desc = request.form["job_description"]
    results = []
    for file in resume_files:
        if file.filename.endswith(".pdf"):
            resume_text = extract_text(file)
        elif file.filename.endswith(".docx"):
            resume_text = extract_text_docx(file)
        else:
            return "Unsupported file type.", 400
        result = screen_resume(resume_text, job_desc)
        questions = generate_interview_questions(resume_text, job_desc)
        ats=generate_ats_score(resume_text)
        skill_gap=generate_skill_gap(resume_text, job_desc)
        career_roadmap=generate_career_roadmap(resume_text)
        results.append({
            "filename": file.filename,
            "result": result,
            "questions": questions,
            "ats" : ats,
            "skill_gap": skill_gap,
            "career_roadmap": career_roadmap
        })
        save_history(file.filename, result) 
    return render_template("result.html", results=results)
@app.route("/scrape", methods=["POST"])
def scrape():
    url=request.form["url"]
    result=scrape_job_description(url)
    return result
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))