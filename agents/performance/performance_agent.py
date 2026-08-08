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
            "performances using match statistics."
        ),

        llm=llm,

        verbose=True
    )


def run_performance_agent(match_context):

    agent = create_performance_agent()

    task = Task(

        description=f"""
        {match_context.to_prompt()}

        Analyze the team's recent performance.

        Include:

        - Batting performance
        - Bowling performance
        - Fielding performance
        - Best performers
        - Areas that need improvement

        If actual performance statistics are not available,
        clearly state that the analysis is based on the
        available match context rather than inventing statistics.
        """,

        expected_output="""
        A complete performance analysis report with
        strengths and weaknesses.
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