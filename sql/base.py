from abc import ABC, abstractmethod
from typing import Dict, Any
from supabase import Client

class BaseSupabase(ABC):
    def __init__(self, client: Client):
        self.client = client

    @abstractmethod
    def run(self, input_params: Dict[str, Any]) -> Any:
        pass


class Query(BaseSupabase):
    @abstractmethod
    def get_query(self, input_params: Dict[str, Any]):
        """
        Return the supabase query builder object configured based on input_params.
        """
        pass

    def run(self, input_params: Dict[str, Any]) -> Dict[str, Any]:
        response = self.get_query(input_params)
        
        if response:
            return response
        else:
            raise Exception(f"Supabase query error: {response.error.message}")


class Mutation(BaseSupabase):
    @abstractmethod
    def get_mutation(self, input_params: Dict[str, Any]):
        """
        Return the supabase query builder for the mutation (insert/update/delete).
        """
        pass

    def run(self, input_params: Dict[str, Any]) -> Dict[str, Any]:
        mutation_builder = self.get_mutation(input_params)
        response = mutation_builder.execute()
        if response:
                 return {
            "data": response.data,
            "count": response.count  # number of rows affected, if available
        }

        else:
            raise Exception(f"Supabase mutation error: {response.error.message}")
   