from crewai import Task, Crew, Process
from agents.planner.planner import planner_agent

planning_task = Task(
    description="""
A coach asks:

'I have a cricket match tomorrow.
Which specialist agents should help me prepare?'

Explain which agents should be involved and why.
""",
    expected_output="A list of specialist agents with a short reason for each.",
    agent=planner_agent
)

crew = Crew(
    agents=[planner_agent],
    tasks=[planning_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()

print("\n========================")
print("MATCHMIND AI RESPONSE")
print("========================\n")

print(result)