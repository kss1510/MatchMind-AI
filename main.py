from crewai import Task, Crew, Process

from agents.planner.planner import planner_agent
from config.prompts import PLANNER_TASK

user_request = """
I have a cricket match tomorrow.
Which specialist agents should help me prepare?
"""

planning_task = Task(
    description=PLANNER_TASK.format(
        user_request=user_request
    ),
    expected_output="""
A valid JSON object containing the selected MatchMind AI agents and the reason for each selection.
""",
    agent=planner_agent
)

crew = Crew(
    agents=[planner_agent],
    tasks=[planning_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n==============================")
print("MATCHMIND AI")
print("==============================\n")

print(result)