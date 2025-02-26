import os
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv('APP_PORT', '3000'))