from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env.local'))


url = os.getenv('DATABASE_URL')
key = os.getenv('DATABASE_KEY')
SUPABASE_CONFIG = {
    "url": url,
    "key": key
}
