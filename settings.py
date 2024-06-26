import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
dot_env = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dot_env)

DATA_BASE_URL = os.getenv('DATA_BASE_URL')



