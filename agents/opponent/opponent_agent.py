from crewai import Agent, Task, Crew, Process
from config.settings import llm


class OpponentAgent:

    def __init__(self):

        self.agent = Agent(
            role="Opponent Analysis Specialist",

            goal="""
            Analyze the opponent team and identify their strengths,
            weaknesses, key players, and possible match-winning strategies.
            """,

            backstory="""
            You are an experienced cricket analyst who studies opponent teams,
            player statistics, recent performances, and tactical patterns to
            help teams prepare effectively.
            """,

            llm=llm,

            verbose=True
        )

    def run(self, user_request, match_context):

        task = Task(

            description=f"""
            {match_context.to_prompt()}

            {user_request}

            Analyze the opponent and include:

            - Team strengths
            - Team weaknesses
            - Key players
            - Batting analysis
            - Bowling analysis
            - Suggested strategy against this opponent
            """,

            expected_output="""
            A detailed opponent analysis report with actionable recommendations.
            """,

            agent=self.agent
        )

        crew = Crew(

            agents=[self.agent],

            tasks=[task],

            process=Process.sequential,

            verbose=True
        )

        return crew.kickoff()