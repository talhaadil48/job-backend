from typing import Dict, Any
from sql import Mutation

class UpdateApplicationById(Mutation):
    def get_mutation(self, input_params: Dict[str, Any]):
        application_id = input_params.pop("application_id")
        status = input_params.pop("status")
        return self.client.table("applications").update({"status":status}).eq("id", application_id)