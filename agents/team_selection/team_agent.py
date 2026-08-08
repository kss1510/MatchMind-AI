from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_team_selection_agent():

    return Agent(

        role="Cricket Team Selection Specialist",

        goal=(
            "Analyze the match context and recommend the most suitable "
            "playing XI for the cricket team."
        ),

        backstory=(
            "You are an experienced cricket selector who evaluates "
            "player roles, match conditions, team balance and opposition "
            "to recommend the best possible playing XI."
        ),

        llm=llm,

        verbose=True
    )


def run_team_selection_agent(match_context):

    agent = create_team_selection_agent()

    task = Task(

        description=f"""
        {match_context.to_prompt()}

        Recommend a suitable playing XI for the team.

        Consider:

        - Match format
        - Opposition
        - Venue
        - Team balance
        - Batting depth
        - Bowling combination
        - All-rounders
        - Tactical requirements

        Clearly explain why the selected players or player roles
        are suitable for this match.
        """,

        expected_output="""
        A playing XI recommendation with roles and
        reasoning for the selection.
        """,

        agent=agent
    )

    crew = Crew(

        agents=[agent],

        tasks=[task],

        process=Process.sequential,

        verbose=True
    )

    return crew.kickoff()