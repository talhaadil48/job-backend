from typing import Dict, Any
from sql import Mutation

class InsertCandidate(Mutation):
    """
    Insert a new candidate into the 'candidates' table.
    Expects input_params with keys: user_id, resume_url, bio, skills, experience_years, education, linkedin_url, portfolio_url
    """

    def get_mutation(self, input_params: Dict[str, Any]):
        data = {
            "user_id": input_params["user_id"],
            "resume_url": input_params.get("resume_url", None),
            "bio": input_params.get("bio", None),
            "skills": input_params.get("skills", []),  # skills is a text[]
            "experience_years": input_params.get("experience_years", None),
            "education": input_params.get("education", None),
            "linkedin_url": input_params.get("linkedin_url", None),
           
        }
        return self.client.table("candidates").insert(data)
