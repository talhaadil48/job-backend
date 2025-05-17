
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


def delete_job(job_id):
    response = requests.post(f"{BASE_URL}/deljob", json={
        "job_id": job_id
    })
    print("[DELETE JOB]", response.status_code, response.json())
    
    



def delete_user(user_id):
    response = requests.post(f"{BASE_URL}/deluser", json={
        "user_id": user_id
    })
    print("[DELETE USER]", response.status_code, response.json())
    


import requests

BASE_URL = "http://localhost:8000"

def update_user(user_data):
    response = requests.post(f"{BASE_URL}/updateuser", json=user_data)
    print("[UPDATE USER]", response.status_code, response.json())


candidate_user_payload = {
    "user_id": "2e4f35c8-e161-48d5-93ce-79c4e88b1440",  # replace with a valid UUID in your system
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "password_hash": "hashedpassword123",
    "role": "candidate",
    "is_blocked": False,
    "profile_picture_url": "https://xyz.supabase.co/storage/v1/avatar/alice.jpg",

    "resume_url": "https://xyz.supabase.co/resumes/alice_resume.pdf",
    "skills": ["Python", "FastAPI", "SQL"],
    "experience_years": 4,
    "education": "M.Sc. Computer Science",
    "linkedin_url": "https://linkedin.com/in/alicejohnson",
    "portfolio_url": "https://alice.dev"
}

#
employer_user_payload = {
    "user_id": "143ba632-bdc1-4834-a2dc-3927e471e87f",  # replace with a valid UUID in your system
    "name": "Bob Corp",
    "email": "bob@bobcorp.com",
    "role": "employer",
    "is_blocked": False,
    "profile_picture_url": "https://xyz.supabase.co/storage/v1/avatar/bobcorp.jpg",
    "company_name": "Bob Corp Ltd.",
    "company_website": "https://bobcorp.com",
    
}

def get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    print("[GET USER]", response.status_code, response.json())
    
    
def test_get_job(job_id):
    response = requests.get(f"{BASE_URL}/job/{job_id}")
    print("[GET JOB]", response.status_code)
    try:
        print(response.json())
    except Exception:
        print(response.text)

def get_application_by_id(application_id):
    response = requests.get(f"{BASE_URL}/application/{application_id}")
    print("[GET APPLICATION]", response.status_code)
    try:
        print(response.json())
    except Exception:
        print(response.text)


def test_get_all_jobs():
    response = requests.get(f"{BASE_URL}/alljobs")
    print("[GET ALL JOBS]", response.status_code)
    try:
        print(response.json())
    except Exception:
        print(response.text)
        
        
def test_get_all_users():
    response = requests.get(f"{BASE_URL}/allusers")
    print("[GET ALL JOBS]", response.status_code)
    try:
        print(response.json())
    except Exception:
        print(response.text)
        
        
def test_get_user_by_email_and_role(email, role):
    response = requests.get(f"{BASE_URL}/user_by_email_role", params={"email": email, "role": role})
    print("[GET USER BY EMAIL AND ROLE]", response.status_code)
    try:
        print(response.json())
    except Exception:
        print(response.text)
        
test_get_user_by_email_and_role("cathy.candidate@exampe.com","candidate")
