from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser
from config.match_context import MatchContext
from orchestrator.agent_manager import AgentManager


MATCH_ID = 40381


print("=" * 60)
print("MATCHMIND AI - STEP 3 DATA INTEGRATION")
print("=" * 60)


try:

    # ---------------------------------------------------------
    # 1. Create API client
    # ---------------------------------------------------------

    client = CricbuzzClient()

    print("\nFetching match information...")

    match_info_raw = client.get_match_info(MATCH_ID)

    print("Match information fetched!")


    # ---------------------------------------------------------
    # 2. Parse match information
    # ---------------------------------------------------------

    parsed_match_info = CricbuzzParser.parse_match_info(
        match_info_raw
    )

    print("Match information parsed!")


    # ---------------------------------------------------------
    # 3. Fetch scorecard
    # ---------------------------------------------------------

    print("\nFetching scorecard...")

    scorecard_raw = client.get_scorecard(MATCH_ID)

    print("Scorecard fetched!")


    # ---------------------------------------------------------
    # 4. Parse scorecard
    # ---------------------------------------------------------

    parsed_scorecard = CricbuzzParser.parse_scorecard(
        scorecard_raw
    )

    print("Scorecard parsed!")


    # ---------------------------------------------------------
    # 5. Create MatchContext using REAL DATA
    # ---------------------------------------------------------

    match_context = MatchContext(
        team=parsed_match_info["team1"],
        opponent=parsed_match_info["team2"],
        format=parsed_match_info["format"],
        venue=parsed_match_info["venue"],
        match_date=parsed_match_info["start_date"],
        match_data=parsed_match_info,
        scorecard=parsed_scorecard
    )

    print("Match context created successfully!")


    # ---------------------------------------------------------
    # 6. Display context
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("MATCH CONTEXT")
    print("=" * 60)

    print(match_context.to_prompt())


    # ---------------------------------------------------------
    # 7. Create Agent Manager
    # ---------------------------------------------------------

    manager = AgentManager()


    # ---------------------------------------------------------
    # 8. Select specialist agents
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
    # 9. Execute agents
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("MATCHMIND AI - MULTI-AGENT EXECUTION")
    print("=" * 60)

    results = manager.execute_agents(
        selected_agents,
        match_context
    )


    # ---------------------------------------------------------
    # 10. Display results
    # ---------------------------------------------------------

    for result in results:

        print("\n" + "=" * 60)
        print(result["agent"])
        print("=" * 60)

        print(result["result"])


    # ---------------------------------------------------------
    # 11. Success
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("MATCHMIND AI STEP 3 DATA INTEGRATION SUCCESSFUL!")
    print("=" * 60)


except Exception as e:

    print("\n" + "=" * 60)
    print("STEP 3 DATA INTEGRATION FAILED!")
    print("=" * 60)

    print("\nError Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)