def build_prompt(resume_text, job_desc):
    return f"""
You are an expert HR recruiter. Given the resume and job description below, evaluate the candidate.

Job Description:
{job_desc}

Resume:
{resume_text}

Provide:
1. Fit Score: out of 10
2. Strengths:
3. Missing Skills:
"""
def build_interview_prompt(resume_text, job_desc):
    return f"""
Given this resume and job description, generate exactly 5 interview questions that target the candidate's weak areas and skill gaps. Number them 1-5.

Job Description:
{job_desc}

Resume:
{resume_text}

Interview Questions:
"""
def build_ats_prompt(resume_text):
    return f"""
You are an ATS (Applicant Tracking System) expert. Please Analyze this resume and provide:
1. ATS Score:: out of 10
2. Missing keywords: list important keywords that are absent
3. Formatting Issues: list any formatting problems that would confuse an ATS
4. Section Check: which of these are present or absent - Summary, Experience, Skills, Certifications, Education 

Resume:
{resume_text}

Be specific and concise
"""
def build_skill_gap_prompt(resume_text, job_desc):
    return f"""
You have to return a table like this : Skill | Present in Resume | Gap Level (High/Medium/Low/None)
1. Extract required skills from the job description
2. Check each against the resume
3. Return exactly in that table format - no extra text

Job Description:
{job_desc}

Resume:
{resume_text}

"""
def build_career_roadmap_prompt(resume_text):
    return f"""
You are a career counselor. Based on this resume, suggest a personalized career roadmap.
1. 2-3 possible career paths based on the current skills
2. Skill to learn each path
3. Suggested timeline (3 months, 6 months, 1 year)
4. Recommend resources (E-learning platforms, books, research papers)

Resume:
{resume_text}
"""