from typing import Dict, Any
from sql import Mutation

class DeleteJobById(Mutation):
    """
    Delete a job from the 'jobs' table by its ID.
    Expects input_params with key: job_id
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        job_id = input_params["job_id"]
        return self.client.table("jobs").delete().eq("id", job_id)
