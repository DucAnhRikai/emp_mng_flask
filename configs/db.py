import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = str(os.getenv("DB_URI", ""))