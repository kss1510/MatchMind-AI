from crewai import Agent
from crewai.llm import LLM

from config.settings import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    VERBOSE,
)

llm = LLM(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL
)

planner_agent = Agent(
    role="Planner Agent",
    goal="Select the correct MatchMind AI specialist agents for every user request.",
    backstory=(
        "You are the coordinator of MatchMind AI. "
        "You never solve sports problems yourself. "
        "Your responsibility is to analyze the user's request and choose "
        "the appropriate specialist agents from the predefined list."
    ),
    llm=llm,
    verbose=VERBOSE
)