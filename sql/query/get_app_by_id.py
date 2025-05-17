from typing import Dict, Any
from sql import Query

class GetApplicationById(Query):
    def get_query(self, input_params: Dict[str, Any]):
        application_id = input_params["application_id"]

        # 1. Get the application
        application_res = (
            self.client.table("applications")
            .select("*")
            .eq("id", application_id)
            .execute()
        )
        if not application_res.data:
            return {"error": "Application not found"}
        application = application_res.data[0]

        result = {"application": application}

        # 2. Get the job related to this application
        job_id = application["job_id"]
        job_res = (
            self.client.table("jobs")
            .select("*")
            .eq("id", job_id)
            .execute()
        )
        if not job_res.data:
            return {"error": "Job not found"}
        job = job_res.data[0]
        result["job"] = job

        # 3. Get the employer user from job
        employer_user_id = job["employer_id"]
        employer_user_res = (
            self.client.table("users")
            .select("*")
            .eq("id", employer_user_id)
            .execute()
        )
        if not employer_user_res.data:
            return {"error": "Employer user not found"}
        employer_user = employer_user_res.data[0]
        result["employer_user"] = employer_user

        # 4. Get employer details from employer user id
        employer_res = (
            self.client.table("employers")
            .select("*")
            .eq("user_id", employer_user_id)
            .execute()
        )
        result["employer"] = employer_res.data[0] if employer_res.data else None

        # 5. Get candidate user from application
        candidate_user_id = application["candidate_id"]
        candidate_user_res = (
            self.client.table("users")
            .select("*")
            .eq("id", candidate_user_id)
            .execute()
        )
        if not candidate_user_res.data:
            return {"error": "Candidate user not found"}
        candidate_user = candidate_user_res.data[0]
        result["candidate_user"] = candidate_user

        # 6. Get candidate details from candidate user id
        candidate_res = (
            self.client.table("candidates")
            .select("*")
            .eq("user_id", candidate_user_id)
            .execute()
        )
        result["candidate"] = candidate_res.data[0] if candidate_res.data else None

        return result
