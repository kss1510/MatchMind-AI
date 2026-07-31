from crewai import Agent
from crewai.llm import LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

planner_agent = Agent(
    role="Planner Agent",
    goal="Analyze the user's sports request and decide which specialist agents should handle it.",
    backstory=(
        "You are the coordinator of MatchMind AI. "
        "Your responsibility is to understand the user's request and "
        "identify which agents should be involved."
    ),
    llm=llm,
    verbose=True
)