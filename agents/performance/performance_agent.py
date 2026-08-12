from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_performance_agent():

    return Agent(
        role="Cricket Performance Analyst",

        goal=(
            "Analyze player and team performances "
            "to identify strengths, weaknesses and "
            "improvement opportunities."
        ),

        backstory=(
            "You are a professional cricket performance analyst "
            "who evaluates batting, bowling and fielding "
            "performances using available match statistics."
        ),

        llm=llm,
        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )


def run_performance_agent(match_context):

    agent = create_performance_agent()

    task = Task(
        description=f"""
{match_context.to_prompt()}

Based ONLY on the scorecard above, give a brief performance report.
1. Best batting performance (top scorer: name, runs, strike rate)
2. Best bowling performance (top bowler: name, wickets, economy)
3. Overall match assessment in 1-2 sentences

Use only statistics shown. If data missing, say so.
""",

        expected_output="""
A concise performance report with 3 sections:
1. Best Batting Performance
2. Best Bowling Performance
3. Overall Assessment
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