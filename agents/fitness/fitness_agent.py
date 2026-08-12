from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_fitness_agent():

    return Agent(

        role="Cricket Fitness and Availability Analyst",

        goal=(
            "Evaluate player fitness, workload and availability "
            "to identify potential fitness-related concerns "
            "that could affect team selection and match strategy."
        ),

        backstory=(
            "You are a cricket fitness analyst who evaluates "
            "player workload, fitness indicators and availability "
            "to help coaches make informed decisions."
        ),

        llm=llm,

        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )


def run_fitness_agent(match_context):

    agent = create_fitness_agent()

    task = Task(

        description=f"""
{match_context.to_prompt()}

Based ONLY on the scorecard above, give a brief fitness report.
1. Players with high workload (many overs bowled or long batting innings)
2. Players who may need rest (low contribution)
3. Fitness recommendation for the next match

Use only statistics shown. If data missing, say so.
""",

        expected_output="""
A concise fitness report with 3 sections:
1. High Workload Players
2. Rest Candidates
3. Fitness Recommendation
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