from typing import Dict, Any
from sql import Mutation
class InsertUser(Mutation):
    """
    Insert a new user into the 'users' table in Supabase.
    Expects input_params with keys: id, name, email, password_hash, role, is_blocked, profile_picture_url
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        data = {
            "name": input_params["name"],
            "email": input_params["email"],
            "password_hash": input_params["password_hash"],
            "role": input_params["role"],
            "is_blocked": input_params.get("is_blocked", False),
            "profile_picture_url": input_params.get("profile_picture_url",None)
        }
        return self.client.table("users").insert(data)
