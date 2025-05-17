from sql import Query
from typing import Dict,Any
class GetJobById(Query):
    def get_query(self, input_params: Dict[str, Any]):
        job_id = input_params["job_id"]

        job_data = (
            self.client.table("jobs")
            .select("*, users(*), employers(*)")
            .eq("id", job_id)
            .execute()
        )

        if not job_data.data:
            return {"error": "Job not found"}

        return {"job": job_data.data[0]}
