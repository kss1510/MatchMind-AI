from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_report_agent():

    return Agent(

        role="Cricket Report Generator",

        goal=(
            "Combine reports from multiple cricket analysis agents "
            "into one complete match report."
        ),

        backstory=(
            "You are responsible for merging reports from multiple "
            "specialized cricket agents into one professional report."
        ),

        llm=llm,

        verbose=True
    )


def run_report_agent(
    strategy_report,
    opponent_report,
    team_report,
    performance_report,
    fitness_report
):

    agent = create_report_agent()

    task = Task(

        description=f"""
Combine the following reports into one final cricket report.

Strategy Report:
{strategy_report}

Opponent Analysis:
{opponent_report}

Team Selection:
{team_report}

Performance Analysis:
{performance_report}

Fitness Report:
{fitness_report}

Requirements:

- Remove duplicate information.
- Organize into sections.
- Make it professional.
- End with Final Recommendations.
""",

        expected_output="""
A professional cricket report containing
all agent outputs in one document.
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