from fastapi import HTTPException, Query as FastAPIQuery
from db import SupabaseConnection
from sql.query import GetUserByEmailAndRole, GetUserById, GetJobById, GetApplicationById, GetAllJobs, GetAllUsersWithDetails
from .base import BaseRouter


class GetRoutes(BaseRouter):
    def __init__(self):
        super().__init__()
        self.router.add_api_route("/user/{user_id}", self.get_user_by_id, methods=["GET"])
        self.router.add_api_route("/job/{job_id}", self.get_job_by_id, methods=["GET"])
        self.router.add_api_route("/application/{application_id}", self.get_application_by_id, methods=["GET"])
        self.router.add_api_route("/alljobs", self.get_all_jobs, methods=["GET"])
        self.router.add_api_route("/allusers", self.get_all_users, methods=["GET"])
        self.router.add_api_route("/user_by_email_role", self.get_user_by_email_and_role, methods=["GET"])  # <-- New route

    async def get_user_by_id(self, user_id: str):
        client = SupabaseConnection.get_client()
        query_obj = GetUserById(client)
        try:
            result = query_obj.run({"user_id": user_id})
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_job_by_id(self, job_id: str):
        client = SupabaseConnection.get_client()
        query_obj = GetJobById(client)
        try:
            result = query_obj.run({"job_id": job_id})
            if "error" in result:
                raise HTTPException(status_code=404, detail=result["error"])
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_application_by_id(self, application_id: str):
        client = SupabaseConnection.get_client()
        query_obj = GetApplicationById(client)
        try:
            result = query_obj.run({"application_id": application_id})
            if "error" in result:
                raise HTTPException(status_code=404, detail=result["error"])
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_all_jobs(self):
        client = SupabaseConnection.get_client()
        query_obj = GetAllJobs(client)
        try:
            result = query_obj.run({})
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_all_users(self):
        client = SupabaseConnection.get_client()
        query_obj = GetAllUsersWithDetails(client)
        try:
            result = query_obj.run({})
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_user_by_email_and_role(self, email: str = FastAPIQuery(...), role: str = FastAPIQuery(...)):
        client = SupabaseConnection.get_client()
        query_obj = GetUserByEmailAndRole(client)
        try:
            result = query_obj.run({"email": email, "role": role})
            if "error" in result:
                raise HTTPException(status_code=404, detail=result["error"])
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
