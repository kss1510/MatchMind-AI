from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_team_selection_agent():

    return Agent(
        role="Cricket Team Selection Specialist",

        goal=(
            "Select the best possible playing XI "
            "based on match conditions, player form, "
            "fitness and team balance."
        ),

        backstory=(
            "You are an experienced cricket selector who "
            "analyzes player performance, fitness, pitch "
            "conditions and opposition before selecting "
            "the final playing XI."
        ),

        llm=llm,
        verbose=True
    )


def run_team_selection_agent():

    agent = create_team_selection_agent()

    task = Task(

        description="""
        Select the best playing XI for tomorrow's cricket match.

        Include:
        - Opening batsmen
        - Middle order
        - All-rounders
        - Wicket keeper
        - Fast bowlers
        - Spinners

        Explain why each player is selected.
        """,

        expected_output="""
        A detailed playing XI with player roles
        and selection justification.
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