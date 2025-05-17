from typing import Dict, Any
from sql import Query
class GetUserByEmailAndRole(Query):
    def get_query(self, input_params: Dict[str, Any]):
        email = input_params.get("email")
        role = input_params.get("role")

        if not email or not role:
            return {"error": "Both email and role are required"}

        user_data = (
            self.client.table("users")
            .select("*")
            .eq("email", email)
            .eq("role", role)
            .execute()
        )

        if not user_data.data:
            return {"error": "User not found"}

        return user_data.data[0]
