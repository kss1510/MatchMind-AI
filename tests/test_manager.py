from orchestrator.agent_manager import AgentManager


manager = AgentManager()


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
    }
]


results = manager.execute_agents(selected_agents)


for result in results:
    print("\n" + "=" * 40)
    print(result["agent"])
    print("=" * 40)
    print(result["result"].raw)