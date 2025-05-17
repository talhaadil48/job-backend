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
    InsertCandidate
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
        profile_picture_url: str | None = None
  
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
        portfolio_url: Optional[str] = None
        
    def insert_candidate(self, request:CandidateCreate):
        client = SupabaseConnection.get_client()
        mutation_obj = InsertCandidate(client)
        try:
            result = mutation_obj.run(request.model_dump())
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
