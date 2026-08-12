from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_opponent_agent():

    return Agent(
        role="Cricket Opponent Analyst",

        goal=(
            "Analyze the opposing cricket team's strengths, "
            "weaknesses, key players and tactical vulnerabilities."
        ),

        backstory=(
            "You are an experienced cricket opposition analyst. "
            "You study opponent batting and bowling performances "
            "to identify threats, weaknesses and tactical opportunities."
        ),

        llm=llm,
        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )


def run_opponent_agent(match_context):

    agent = create_opponent_agent()

    task = Task(
        description=f"""
{match_context.to_prompt()}

Based ONLY on the scorecard above, give a brief opponent analysis.
1. Opponent key batsmen (highest scorers with strike rates)
2. Opponent key bowlers (most wickets, best economy)
3. Main tactical threat to address

Use only statistics shown. If data missing, say so.
""",

        expected_output="""
A concise opponent analysis with 3 sections:
1. Key Batsmen
2. Key Bowlers
3. Main Tactical Threat
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