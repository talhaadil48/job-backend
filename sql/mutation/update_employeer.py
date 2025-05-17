from typing import Dict, Any
from sql import Mutation
class UpdateEmployerById(Mutation):
    def get_mutation(self, input_params: Dict[str, Any]):
        user_id = input_params.pop("user_id")
        fields = {
            k: v for k, v in input_params.items()
            if k in {"company_name", "company_website", "company_description", "company_logo_url"}
        }
        return self.client.table("employers").update(fields).eq("user_id", user_id)
