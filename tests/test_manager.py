from orchestrator.agent_manager import AgentManager
from config.match_context import MatchContext


# --------------------------------------------------
# Create Match Context
# --------------------------------------------------

match_context = MatchContext(
    team="India",
    opponent="Australia",
    format="ODI",
    venue="Wankhede Stadium",
    match_date="2026-08-10"
)


# --------------------------------------------------
# Create Agent Manager
# --------------------------------------------------

manager = AgentManager(match_context)


# --------------------------------------------------
# Agents selected for this test
# --------------------------------------------------

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


# --------------------------------------------------
# Execute Agents
# --------------------------------------------------

results = manager.execute_agents(selected_agents)


# --------------------------------------------------
# Display Results
# --------------------------------------------------

for result in results:

    print("\n" + "=" * 60)
    print(result["agent"])
    print("=" * 60)

    print(result["result"])