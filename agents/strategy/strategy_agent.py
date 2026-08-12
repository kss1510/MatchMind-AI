from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_strategy_agent():

    return Agent(

        role="Cricket Strategy Analyst",

        goal=(
            "Develop effective cricket strategies based on "
            "match context, team strengths, opponent weaknesses "
            "and available performance information."
        ),

        backstory=(
            "You are an experienced cricket strategist who "
            "studies match situations, playing conditions, "
            "team strengths and opponent weaknesses to "
            "recommend practical tactical decisions."
        ),

        llm=llm,

        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )


def run_strategy_agent(match_context):

    agent = create_strategy_agent()

    task = Task(

        description=f"""
{match_context.to_prompt()}

Based ONLY on the match data above, provide a brief cricket strategy report.

Cover these 3 points:
1. Batting strategy (based on actual scores/strike rates)
2. Bowling strategy (based on actual wickets/economy)
3. Key tactical priority for the next match

Use only facts from the data. If data is missing, say so.
""",

        expected_output="""
A concise strategy report with exactly 3 sections:
1. Batting Strategy
2. Bowling Strategy
3. Key Tactical Priority
""",

        agent=agent
    )

    crew = Crew(

        agents=[agent],

        tasks=[task],

        process=Process.sequential,

        verbose=False
    )

    return crew.kickoff()