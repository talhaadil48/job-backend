from typing import Dict, Any
from sql import Mutation

class InsertJob(Mutation):
    """
    Insert a new job into the 'jobs' table.
    Expects input_params with keys: employer_id, title, description, type, tags, salary, deadline
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        data = {
            "employer_id": input_params["employer_id"],
            "title": input_params["title"],
            "description": input_params.get("description", None),
            "type": input_params.get("type", None),
            "tags": input_params.get("tags", []),  # tags is a text[]
            "salary": input_params.get("salary", None),
            "deadline": input_params.get("deadline", None)  # expected as a date string 'YYYY-MM-DD'
        }
        return self.client.table("jobs").insert(data)
