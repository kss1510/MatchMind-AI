from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_fitness_agent():

    return Agent(

        role="Cricket Fitness Specialist",

        goal=(
            "Evaluate fitness considerations relevant to the "
            "team and identify potential fitness concerns."
        ),

        backstory=(
            "You are a cricket fitness and workload specialist "
            "who helps teams assess player fitness, workload "
            "and preparation requirements before matches."
        ),

        llm=llm,

        verbose=True
    )


def run_fitness_agent(match_context):

    agent = create_fitness_agent()

    task = Task(

        description=f"""
        {match_context.to_prompt()}

        Provide a fitness and preparation analysis for the team.

        Include:

        - General fitness considerations
        - Workload considerations
        - Match preparation
        - Recovery considerations
        - Potential fitness risks

        Do not invent medical conditions or specific player injuries.
        If player fitness data is unavailable, clearly state that
        actual fitness status cannot be determined from the
        available information.
        """,

        expected_output="""
        A cricket fitness and preparation report containing
        practical recommendations and clearly stated limitations.
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