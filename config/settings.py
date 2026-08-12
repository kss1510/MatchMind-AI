from crewai.llm import LLM
import os
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = "NA-OLLAMA-LOCAL-ONLY" # Proves we don't use real OpenAI

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

OLLAMA_MODEL = "ollama/llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434"

TEMPERATURE = 0.3
VERBOSE = False

llm = LLM(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=TEMPERATURE,
    timeout=300
)