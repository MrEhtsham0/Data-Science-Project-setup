import os
import logging
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
log_path = os.path.join(os.getcwd(),"logs","LOF_FILE")
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

#setup basic configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] - %(levelname)s - %(name)s -   %(message)s",
    level=logging.INFO
)
