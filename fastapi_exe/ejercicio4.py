import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List
from transformers import pipeline




