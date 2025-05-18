import requests
import pdfplumber
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date
from db import SupabaseConnection
from sql.mutation import (
    InsertJob,
    InsertUser,
    InsertEmployer,
    InsertApplication,
    InsertCandidate,
    DeleteJobById,
    DeleteUserById,
    UpdateUserById,
    UpdateJobById,
    UpdateEmployerById,
    UpdateCandidateById,
    UpdateApplicationById
    
    
)
from .base import BaseRouter


class PostRoutes(BaseRouter):
    def __init__(self):
        super().__init__()
        self.router.add_api_route("/job", self.insert_job, methods=["POST"])
        self.router.add_api_route("/user", self.insert_user, methods=["POST"])
        self.router.add_api_route("/employer", self.insert_employer, methods=["POST"])
        self.router.add_api_route("/application", self.insert_application, methods=["POST"])
        self.router.add_api_route("/candidate", self.insert_candidate, methods=["POST"])
        self.router.add_api_route("/deluser", self.delete_user, methods=["POST"])
        self.router.add_api_route("/deljob", self.delete_job, methods=["POST"])
        self.router.add_api_route("/updateuser", self.update_user, methods=["POST"])
        self.router.add_api_route("/updatejob", self.update_job, methods=["POST"])
        self.router.add_api_route("/updateapplication", self.update_application, methods=["POST"])
        self.router.add_api_route("/extract_pdf_text", self.extract_pdf_text, methods=["POST"])

  
    class JobCreate(BaseModel):
        employer_id: str
        title: str
        description: Optional[str] = None
        type: Optional[str] = None
        tags: List[str] = []
        salary: Optional[str] = None
        deadline: str
    def insert_job(self, request:JobCreate):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertJob(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    class UserCreate(BaseModel):
        name: str
        email: str
        password_hash: str
        role: str
        is_blocked: bool = False
        profile_picture_url: Optional[str] | None
  
    def insert_user(self, request:UserCreate):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertUser(client)
        try:
            result = mutation_obj.run(request.model_dump())
            print(result)
            return result
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))

    class EmployerCreate(BaseModel):
        user_id: str
        company_name: str
        company_website: Optional[str] = None
        company_description: Optional[str] = None
        company_logo_url: Optional[str] = None


    def insert_employer(self, request:EmployerCreate):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertEmployer(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
    class ApplicationCreate(BaseModel):
        candidate_id: str
        job_id: str
        resume_url: str
        message: Optional[str] = None
        status: Optional[str] = "pending"
          

    def insert_application(self, request:ApplicationCreate):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertApplication(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    class CandidateCreate(BaseModel):
        user_id: str
        resume_url: Optional[str] = None
        bio: Optional[str] = None
        skills: List[str] = []
        experience_years: Optional[int] = 0
        education: Optional[str] = None
        linkedin_url: Optional[str] = None
        
        
    def insert_candidate(self, request:CandidateCreate):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertCandidate(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
        
    class DeleteJob(BaseModel):
        job_id: str
          

    def delete_job(self, request:DeleteJob):
        client = SupabaseConnection.get_client()
        mutation_obj = DeleteJobById(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        
         
    class DeleteUser(BaseModel):
        user_id: str
          

    def delete_user(self, request:DeleteUser):
        client = SupabaseConnection.get_client()
        mutation_obj = DeleteUserById(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        
    class UserUpdate(BaseModel):
        user_id: str
        name: Optional[str] = None
        email: Optional[str] = None
        password_hash: Optional[str] = None
        role: Optional[str] = None
        is_blocked: Optional[bool] = None
        profile_picture_url: Optional[str] = None

        # Candidate-specific fields
        resume_url: Optional[str] = None
        skills: Optional[List[str]] = None
        experience_years: Optional[int] = None
        education: Optional[str] = None
        linkedin_url: Optional[str] = None
    

        # Employer-specific fields
        company_name: Optional[str] = None
        company_website: Optional[str] = None
        company_description: Optional[str] = None
        company_logo_url: Optional[str] = None


    def update_user(self, request: UserUpdate):
        client = SupabaseConnection.get_client()

        try:
            input_data = request.model_dump(exclude_unset=True)

            # Always update user table
            user_data = {
                k: v for k, v in input_data.items()
                if k in {"name", "email", "password_hash", "role", "is_blocked", "profile_picture_url"}
            }
            user_data["user_id"] = input_data["user_id"]
            UpdateUserById(client).run(user_data)

            # Update candidate or employer table based on role
            role = input_data.get("role")
            if role == "candidate":
                candidate_data = {
                    k: v for k, v in input_data.items()
                    if k in {"resume_url", "skills", "experience_years", "education", "linkedin_url"}
                }
                candidate_data["user_id"] = input_data["user_id"]
                UpdateCandidateById(client).run(candidate_data)

            elif role == "employer":
                employer_data = {
                    k: v for k, v in input_data.items()
                    if k in {"company_name", "company_website", "company_description", "company_logo_url"}
                }
                employer_data["user_id"] = input_data["user_id"]
                UpdateEmployerById(client).run(employer_data)

            return {"status": "success"}

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

        
    class JobUpdate(BaseModel):
        job_id: str
        title: Optional[str] = None
        description: Optional[str] = None
        type: Optional[str] = None
        tags: Optional[List[str]] = None
        salary: Optional[str] = None
        deadline: Optional[str] = None  # Can convert to `date` if needed
    def update_job(self, request:JobUpdate):
        client = SupabaseConnection.get_client()
        mutation_obj = UpdateJobById(client)
        try:
            result = mutation_obj.run(request.model_dump())
            print(result)
            return result
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=str(e))


    class UpdateApplication(BaseModel):
        application_id: str
        candidate_id: Optional[str] = None
        job_id: Optional[str] = None
        resume_url: Optional[str] = None
        message: Optional[str] = None
        status: Optional[str] = None
        applied_at: Optional[str] = None

    def update_application(self, request:UpdateApplication):
        client = SupabaseConnection.get_client()
        mutation_obj = UpdateApplicationById(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    class ResumeRequest(BaseModel):
        url: str

    def extract_pdf_text(self,request: ResumeRequest):
        try:
            # No need to dump model if you just want the url attribute
            response = requests.get(request.url)
            with open("temp.pdf", "wb") as f:
                f.write(response.content)

            text = ""
            with pdfplumber.open("temp.pdf") as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
                    text += "\n"

            return {"text": text.strip()}
        except Exception as e:
            return {"error": str(e)}