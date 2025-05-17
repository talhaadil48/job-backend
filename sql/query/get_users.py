from typing import Dict, Any
from sql import Query
class GetAllUsersWithDetails(Query):
    def get_query(self, input_params: Dict[str, Any] = None):
        users_data = self.client.table("users").select("*").execute()
        if not users_data.data:
            return {"error": "No users found"}

        result = []
        for user in users_data.data:
            user_id = user["id"]
            role = user["role"]
            user_entry = {"user": user}

            if role == "candidate":
                candidate_data = (
                    self.client.table("candidates")
                    .select("*")
                    .eq("user_id", user_id)
                    .execute()
                )
                user_entry["candidate"] = candidate_data.data[0] if candidate_data.data else None

            elif role == "employer":
                employer_data = (
                    self.client.table("employers")
                    .select("*")
                    .eq("user_id", user_id)
                    .execute()
                )
                user_entry["employer"] = employer_data.data[0] if employer_data.data else None

            result.append(user_entry)

        return result
