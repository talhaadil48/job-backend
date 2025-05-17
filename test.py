
import requests
BASE_URL = "http://localhost:8000"
def insert_candidate(user_id):
    response = requests.post(f"{BASE_URL}/candidate", json={
        "user_id": user_id,
        "resume_url": "https://example.com/resume.pdf",
        "bio": "Experienced developer",
        "skills": ["Python", "FastAPI"],
        "experience_years": 3,
        "education": "BS Computer Science",
        "linkedin_url": "https://linkedin.com/in/talhaadil",
        "portfolio_url": "https://talha.dev"
    })
    print("[CANDIDATE]", response.status_code, response.json())



def insert_user():
    response = requests.post(f"{BASE_URL}/user", json={
        "name": "Talha Adil",
        "email": "talhaadil48@icloud.com",
        "password_hash": "hello123",
        "role": "candidate",
        "is_blocked": False,
        "profile_picture_url": None
    })
    print("[USER]", response.status_code, response.json())
    return response.json().get("id")


def insert_employer(user_id):
    response = requests.post(f"{BASE_URL}/employer", json={
        "user_id": user_id,
        "company_name": "OpenAI",
        "company_website": "https://openai.com",
        "company_description": "AI Research",
        "company_logo_url": "https://logo.clearbit.com/openai.com"
    })
    print("[EMPLOYER]", response.status_code, response.json())
    
    
def insert_job(employer_id):
    response = requests.post(f"{BASE_URL}/job", json={
        "employer_id": employer_id,
        "title": "Full Stack Developer",
        "description": "Build AI-powered platforms",
        "type": "Full-time",
        "tags": ["AI", "Python", "React"],
        "salary": "$80,000 - $100,000",
        "deadline": "2025-06-01"
    })
    print("[JOB]", response.status_code, response.json())
    return response.json().get("id")



def insert_application(candidate_id, job_id):
    response = requests.post(f"{BASE_URL}/application", json={
        "candidate_id": candidate_id,
        "job_id": job_id,
        "resume_url": "https://example.com/resume.pdf",
        "message": "Looking forward to this opportunity!"
    })
    print("[APPLICATION]", response.status_code, response.json())


insert_application("3665c5c8-5d89-43b9-b2f6-3f660f02e86a","9ffa351d-46e7-428d-879a-ec82b66f3349")