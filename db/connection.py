
from supabase import create_client, Client
from config import SUPABASE_CONFIG

class SupabaseConnection:
    """
    Manages a single global Supabase client connection.
    """
    _client: Client = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._client is None:
            try:
                print("SUPABASE_CONFIG:", SUPABASE_CONFIG)
                cls._client = create_client(
                    SUPABASE_CONFIG["url"],
                    SUPABASE_CONFIG["key"]
                )
                print("Supabase client initialized.")
            except Exception as e:
                print("Error initializing Supabase client:", e)
                raise e
        return cls._client

    @classmethod
    def close_client(cls):
        # Placeholder if future cleanup is required
        print("Supabase client does not require explicit closing.")
        cls._client = None