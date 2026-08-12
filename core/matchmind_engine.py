from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser
from config.match_context import MatchContext
from orchestrator.agent_manager import AgentManager
from agents.planner.planner import plan_agents
import traceback


class MatchMindEngine:
    """
    Main orchestration engine for MatchMind AI.
    Handles data fetching, context creation, and agent orchestration.
    """

    def __init__(self):
        self.agent_manager = AgentManager()
        self.client = CricbuzzClient()

    def process_match(self, match_id, execute_pipeline=True):
        """
        End-to-end pipeline for a specific match ID.
        If execute_pipeline is False, it will only fetch data and create context.
        """
        print("\n" + "=" * 60)
        print("MATCHMIND AI ENGINE")
        print("=" * 60)

        try:
            print(f"\n[1] Fetching Cricbuzz match data for Match ID: {match_id}...")
            match_info_raw = self.client.get_match_info(match_id)
            scorecard_raw = self.client.get_scorecard(match_id)
            print("[OK] Data fetched successfully")

            print("\n[2] Parsing match data...")
            parsed_match_info = CricbuzzParser.parse_match_info(match_info_raw)
            parsed_scorecard = CricbuzzParser.parse_scorecard(scorecard_raw)
            print("[OK] Data parsed successfully")

            print("\n[3] Creating Match Context...")
            match_context = MatchContext(
                team=parsed_match_info.get("team1", "Unknown Team 1"),
                opponent=parsed_match_info.get("team2", "Unknown Team 2"),
                format=parsed_match_info.get("format", "Unknown Format"),
                venue=parsed_match_info.get("venue", "Unknown Venue"),
                match_date=parsed_match_info.get("start_date", "Unknown Date"),
                match_data=parsed_match_info,
                scorecard=parsed_scorecard
            )
            print("[OK] Match Context created successfully")

            if not execute_pipeline:
                return {
                    "success": True,
                    "match_context": match_context,
                    "message": "Initialization completed (pipeline execution skipped)"
                }

            user_request = (
                f"Provide a complete {match_context.format} cricket analysis for "
                f"{match_context.team} vs {match_context.opponent} at {match_context.venue}. "
                f"Analyze performance, opponent threats, strategy, "
                f"team selection and fitness considerations."
            )

            print("\n[4] Planning analysis...")
            selected_agents = plan_agents(user_request)

            print("\nSelected Agents:")
            for agent in selected_agents:
                print(f"- {agent['agent']}")

            print("\n[5] Executing specialist agents...")
            results = self.agent_manager.execute_agents(
                selected_agents,
                match_context
            )

            final_report = ""
            for result in results:
                if result["agent"] == "Report Generator Agent":
                    final_report = result["result"]
                    break

            print("\n" + "=" * 60)
            print("MATCHMIND AI ANALYSIS COMPLETED")
            print("=" * 60)

            return {
                "success": True,
                "match_context": match_context,
                "user_request": user_request,
                "selected_agents": selected_agents,
                "agent_results": results,
                "final_report": final_report
            }

        except Exception as e:
            print("\n" + "=" * 60)
            print("MATCHMIND AI EXECUTION FAILED")
            print("=" * 60)
            print(f"Error Type: {type(e).__name__}")
            print(f"Error: {e}")
            traceback.print_exc()
            return {
                "success": False,
                "error": str(e)
            }