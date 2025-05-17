from typing import Dict, Any
from sql import Mutation

class DeleteUserById(Mutation):
    """
    Delete a user from the 'users' table by their ID.
    Expects input_params with key: user_id
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        user_id = input_params["user_id"]
        return self.client.table("users").delete().eq("id", user_id)
