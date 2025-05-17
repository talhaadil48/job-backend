from typing import Dict, Any
from sql import Mutation

class UpdateUserById(Mutation):
    """
    Update user information in the 'users' table by their ID.
    Expects input_params with key: user_id and any of the fields to update.
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        user_id = input_params.pop("user_id")
        update_fields = {}

        # Only include valid keys
        allowed_fields = {
            "name", "email", "password_hash", "role", "is_blocked", "profile_picture_url"
        }

        for key in allowed_fields:
            if key in input_params:
                update_fields[key] = input_params[key]

        return self.client.table("users").update(update_fields).eq("id", user_id)
