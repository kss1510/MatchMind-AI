from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_strategy_agent():

    return Agent(
        role="Cricket Strategy Specialist",

        goal=(
            "Analyze cricket match situations and create "
            "effective batting and bowling strategies."
        ),

        backstory=(
            "You are an expert cricket analyst who studies "
            "opponents, pitch conditions, and match scenarios "
            "to recommend winning strategies."
        ),

        llm=llm,
        verbose=True
    )


def run_strategy_agent(match_context):

    agent = create_strategy_agent()

    task = Task(

        description=f"""
        {match_context.to_prompt()}

        Create a match strategy based on this context.

        Include:

        - Batting approach
        - Bowling approach
        - Key tactical decisions
        """,

        expected_output="""
        A cricket strategy report containing batting,
        bowling and tactical recommendations.
        """,

        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return result