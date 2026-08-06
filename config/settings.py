from crewai.llm import LLM

OLLAMA_MODEL = "ollama/llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434"

TEMPERATURE = 0.3
VERBOSE = True

llm = LLM(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=TEMPERATURE
)