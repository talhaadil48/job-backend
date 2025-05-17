from typing import Dict, Any
from sql import Mutation

class InsertApplication(Mutation):
    """
    Insert a new application into the 'applications' table.
    Expects input_params with keys: candidate_id, job_id, resume_url, message
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        data = {
            "candidate_id": input_params["candidate_id"],
            "job_id": input_params["job_id"],
            "resume_url": input_params["resume_url"],
            "message": input_params.get("message", None)
        }
        return self.client.table("applications").insert(data)
