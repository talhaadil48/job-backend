from typing import Dict, Any
from sql import Query

class GetUserById(Query):
    def get_query(self, input_params: Dict[str, Any]):
        user_id = input_params["user_id"]

        user_data = (
            self.client.table("users")
            .select("*")
            .eq("id", user_id)
            .execute()
        )
        if not user_data.data:
            return {"error": "User not found"}

        user = user_data.data[0]
        role = user["role"]

        result = {"user": user}

        if role == "candidate":
            candidate_data = (
                self.client.table("candidates")
                .select("*")
                .eq("user_id", user_id)
                .execute()
            )
            result["candidate"] = candidate_data.data[0] if candidate_data.data else None

            applications_data = (
                self.client.table("applications")
                .select("*, jobs!fk_applications_job(*)")  # join jobs using fk_applications_job
                .eq("candidate_id", user_id)
                .execute()
            )
            result["applications"] = applications_data.data if applications_data.data else []

        elif role == "employer":
            employer_data = (
                self.client.table("employers")
                .select("*")
                .eq("user_id", user_id)
                .execute()
            )
            result["employer"] = employer_data.data[0] if employer_data.data else None

            jobs_data = (
                self.client.table("jobs")
                .select("*")
                .eq("employer_id", user_id)
                .execute()
            )
            jobs = jobs_data.data if jobs_data.data else []
            result["jobs"] = jobs

            job_ids = [job["id"] for job in jobs]

            if job_ids:
                applications_data = (
                    self.client.table("applications")
                    .select("*, candidates!fk_applications_candidate(*)")  # join candidates using fk_applications_candidate
                    .in_("job_id", job_ids)
                    .execute()
                )
                result["applications"] = applications_data.data if applications_data.data else []
            else:
                result["applications"] = []

        return result
