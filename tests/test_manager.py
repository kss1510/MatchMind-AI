from orchestrator.agent_manager import AgentManager
from config.match_context import MatchContext
from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser


# ---------------------------------------------------------
# Initialize Agent Manager
# ---------------------------------------------------------

manager = AgentManager()


# ---------------------------------------------------------
# Fetch Cricbuzz Match Data
# ---------------------------------------------------------

MATCH_ID = 40381

print("\nFetching Cricbuzz match data...")

client = CricbuzzClient()

scorecard_raw = client.get_scorecard(MATCH_ID)

print("Scorecard fetched successfully!")


# ---------------------------------------------------------
# Parse Scorecard
# ---------------------------------------------------------

parsed_scorecard = CricbuzzParser.parse_scorecard(
    scorecard_raw
)

print("Scorecard parsed successfully!")


# ---------------------------------------------------------
# Create Match Context
# ---------------------------------------------------------

match_context = MatchContext(
    team="India",
    opponent="England",
    format="T20",
    venue="Wankhede Stadium",
    match_date="10 August 2026",
    match_data=parsed_scorecard
)

print("Match context created with real Cricbuzz data!")


# ---------------------------------------------------------
# Agents selected by Planner Agent
# ---------------------------------------------------------

selected_agents = [

    {
        "agent": "Strategy Agent",
        "reason": "Need match tactics"
    },

    {
        "agent": "Opponent Analysis Agent",
        "reason": "Need opponent analysis"
    },

    {
        "agent": "Team Selection Agent",
        "reason": "Need best playing XI"
    },

    {
        "agent": "Performance Agent",
        "reason": "Need performance analysis"
    },

    {
        "agent": "Fitness Agent",
        "reason": "Need fitness report"
    }
]


# ---------------------------------------------------------
# Execute Multi-Agent System
# ---------------------------------------------------------

print("\n")
print("=" * 60)
print("MATCHMIND AI - MULTI-AGENT EXECUTION")
print("=" * 60)


results = manager.execute_agents(
    selected_agents,
    match_context
)


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

for result in results:

    print("\n" + "=" * 60)

    print(result["agent"])

    print("=" * 60)

    print(result["result"])


# ---------------------------------------------------------
# Execution Complete
# ---------------------------------------------------------

print("\n")
print("=" * 60)
print("MATCHMIND AI EXECUTION COMPLETED")
print("=" * 60)