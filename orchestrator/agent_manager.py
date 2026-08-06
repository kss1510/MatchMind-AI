from agents.strategy.strategy_agent import run_strategy_agent  
from agents.opponent.opponent_agent import OpponentAgent
from agents.team_selection.team_agent import run_team_selection_agent
class AgentManager:
    """
    Responsible for executing the agents selected by the Planner Agent.
    """

    def __init__(self):

        self.agent_registry = {
            "Strategy Agent": self.strategy_agent,
            "Opponent Analysis Agent": self.opponent_analysis_agent,
            "Team Selection Agent": self.team_selection_agent,
            "Performance Agent": self.performance_agent,
            "Fitness Agent": self.fitness_agent,
            "Report Generator Agent": self.report_generator_agent,
        }


    def strategy_agent(self):

       return run_strategy_agent()



    def opponent_analysis_agent(self):

        agent = OpponentAgent()

        return agent.run(
            """
            Analyze the upcoming opponent.

            Include:

            - Team strengths
            - Team weaknesses
            - Key players
            - Batting analysis
            - Bowling analysis
            - Best strategy against them.
            """
        )


    def team_selection_agent(self):
        return run_team_selection_agent()


    def performance_agent(self):
        return "Performance Agent executed"


    def fitness_agent(self):
        return "Fitness Agent executed"


    def report_generator_agent(self):
        return "Report Generator Agent executed"


    def execute_agents(self, selected_agents):
        """
        Executes agents selected by Planner Agent.
        """

        results = []

        for agent in selected_agents:

            agent_name = agent["agent"]

            if agent_name in self.agent_registry:

                result = self.agent_registry[agent_name]()

                results.append(
                    {
                        "agent": agent_name,
                        "result": result
                    }
                )

        return results