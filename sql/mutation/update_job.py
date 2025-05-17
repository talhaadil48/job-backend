from typing import Dict, Any
from sql import Mutation


class UpdateJobById(Mutation):
    """
    Update job fields in the 'jobs' table by job ID.
    Expects input_params with key: job_id and fields to update.
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        job_id = input_params.pop("job_id")
        allowed_fields = {
            "title", "description", "type", "tags", "salary", "deadline"
        }
        update_fields = {
            key: input_params[key] for key in allowed_fields if key in input_params
        }
        return self.client.table("jobs").update(update_fields).eq("id", job_id)
