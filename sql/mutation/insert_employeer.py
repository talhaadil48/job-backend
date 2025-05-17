from typing import Dict, Any
from sql import Mutation

class InsertEmployer(Mutation):
    """
    Insert a new employer into the 'employers' table.
    Expects input_params with keys: user_id, company_name, company_website, company_description, company_logo_url
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        data = {
            "user_id": input_params["user_id"],
            "company_name": input_params["company_name"],
            "company_website": input_params.get("company_website", None),
            "company_description": input_params.get("company_description", None),
            "company_logo_url": input_params.get("company_logo_url", None)
        }
        return self.client.table("employers").insert(data)
