
from typing import Dict, Any
from sql import Mutation

class UpdateCandidateById(Mutation):
    def get_mutation(self, input_params: Dict[str, Any]):
        user_id = input_params.pop("user_id")
        fields = {
            k: v for k, v in input_params.items()
            if k in {"resume_url", "skills", "experience_years", "education", "linkedin_url"}
        }
        return self.client.table("candidates").update(fields).eq("user_id", user_id)

