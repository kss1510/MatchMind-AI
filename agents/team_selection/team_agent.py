from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_team_selection_agent():

    return Agent(

        role="Cricket Team Selection Analyst",

        goal=(
            "Recommend the most suitable playing combination "
            "based on player roles, match conditions, team balance "
            "and available performance information."
        ),

        backstory=(
            "You are an experienced cricket selector who evaluates "
            "players based on their roles, recent form, match "
            "conditions and team balance to recommend a strong "
            "playing combination."
        ),

        llm=llm,

        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )


def run_team_selection_agent(match_context):

    agent = create_team_selection_agent()

    task = Task(

        description=f"""
{match_context.to_prompt()}

Based ONLY on the scorecard above, give a brief team selection report.
1. Top performers to retain (from batting/bowling stats)
2. Players to reconsider (worst performers)
3. Key selection recommendation

Use only facts from the data. If data is missing, say so.
""",

        expected_output="""
A concise team selection report with 3 sections:
1. Performers to Retain
2. Players to Reconsider
3. Key Recommendation
""",

        agent=agent
    )

    crew = Crew(

        agents=[agent],

        tasks=[task],

        process=Process.sequential,

        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )

    return crew.kickoff()