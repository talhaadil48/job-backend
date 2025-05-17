from typing import Dict, Any
from sql import Mutation

class UpdateApplicationById(Mutation):
    def get_mutation(self, input_params: Dict[str, Any]):
        user_id = input_params.pop("application_id")
        fields = {
            k: v for k, v in input_params.items()
            if k in {"candidate_id", "job_id", "resume_url", "message", "status","applied_at"}
        }
        return self.client.table("application").update(fields).eq("application_id", user_id)

