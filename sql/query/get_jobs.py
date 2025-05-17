from typing import Dict, Any
from sql import Query

class GetAllJobs(Query):
    def get_query(self, input_params: Dict[str, Any]):
        jobs_res = self.client.table("jobs").select("*").execute()
        return {"jobs": jobs_res.data if jobs_res.data else []}
