import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
db_link = os.getenv("database_url")
api_key = os.getenv('api')

db = create_client(db_link,api_key)