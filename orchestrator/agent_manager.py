from agents.strategy.strategy_agent import run_strategy_agent
from agents.opponent.opponent_agent import OpponentAgent
from agents.team_selection.team_agent import run_team_selection_agent
from agents.performance.performance_agent import run_performance_agent
from agents.fitness.fitness_agent import run_fitness_agent
from agents.report.report_agent import run_report_agent

from config.match_context import MatchContext


class AgentManager:
    """
    Responsible for executing agents selected by the Planner Agent
    and combining their outputs into a final report.
    """

    def __init__(self, match_context):

        self.match_context = match_context

        self.agent_registry = {
            "Strategy Agent": self.strategy_agent,
            "Opponent Analysis Agent": self.opponent_analysis_agent,
            "Team Selection Agent": self.team_selection_agent,
            "Performance Agent": self.performance_agent,
            "Fitness Agent": self.fitness_agent,
        }

    # --------------------------------------------------
    # Individual Agents
    # --------------------------------------------------

    def strategy_agent(self):
        return run_strategy_agent(self.match_context)

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
            """,
            self.match_context
        )

    def team_selection_agent(self):
        return run_team_selection_agent(self.match_context)

    def performance_agent(self):
        return run_performance_agent(self.match_context)

    def fitness_agent(self):
        return run_fitness_agent(self.match_context)

    # --------------------------------------------------
    # Report Generator
    # --------------------------------------------------

    def report_generator_agent(
        self,
        strategy_report,
        opponent_report,
        team_report,
        performance_report,
        fitness_report
    ):

        return run_report_agent(
            strategy_report,
            opponent_report,
            team_report,
            performance_report,
            fitness_report
        )

    # --------------------------------------------------
    # Execute Selected Agents
    # --------------------------------------------------

    def execute_agents(self, selected_agents):

        results = []

        reports = {
            "strategy_report": None,
            "opponent_report": None,
            "team_report": None,
            "performance_report": None,
            "fitness_report": None
        }

        # ----------------------------------------------
        # Run selected agents
        # ----------------------------------------------

        for selected_agent in selected_agents:

            agent_name = selected_agent["agent"]

            if agent_name not in self.agent_registry:
                continue

            print(f"\nRunning {agent_name}...")

            result = self.agent_registry[agent_name]()

            if hasattr(result, "raw"):
                output = result.raw
            else:
                output = str(result)

            # Store reports
            if agent_name == "Strategy Agent":
                reports["strategy_report"] = output

            elif agent_name == "Opponent Analysis Agent":
                reports["opponent_report"] = output

            elif agent_name == "Team Selection Agent":
                reports["team_report"] = output

            elif agent_name == "Performance Agent":
                reports["performance_report"] = output

            elif agent_name == "Fitness Agent":
                reports["fitness_report"] = output

            results.append(
                {
                    "agent": agent_name,
                    "result": output
                }
            )

        # ----------------------------------------------
        # Generate final report
        # ----------------------------------------------

        required_reports = [
            reports["strategy_report"],
            reports["opponent_report"],
            reports["team_report"],
            reports["performance_report"],
            reports["fitness_report"]
        ]

        if all(required_reports):

            print("\nRunning Report Generator Agent...")

            final_report = self.report_generator_agent(
                reports["strategy_report"],
                reports["opponent_report"],
                reports["team_report"],
                reports["performance_report"],
                reports["fitness_report"]
            )

            if hasattr(final_report, "raw"):
                final_output = final_report.raw
            else:
                final_output = str(final_report)

            results.append(
                {
                    "agent": "Report Generator Agent",
                    "result": final_output
                }
            )

        return results