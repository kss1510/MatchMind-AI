from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser
from config.match_context import MatchContext
from agents.performance.performance_agent import run_performance_agent


MATCH_ID = 40381


print("=" * 60)
print("MATCHMIND AI - PERFORMANCE AGENT TEST")
print("=" * 60)


try:

    # -----------------------------
    # 1. Fetch match data
    # -----------------------------

    client = CricbuzzClient()

    scorecard_raw = client.get_scorecard(MATCH_ID)

    print("\nAPI call successful!")


    # -----------------------------
    # 2. Parse scorecard
    # -----------------------------

    parsed_scorecard = CricbuzzParser.parse_scorecard(scorecard_raw)

    print("Scorecard parsed successfully!")


    # -----------------------------
    # 3. Create match context
    # -----------------------------

    context = MatchContext(
        team="India",
        opponent="England",
        format="T20",
        venue="Wankhede Stadium",
        match_date="10 August 2026"
    )

    print("Match context created successfully!")


    # -----------------------------
    # 4. Run Performance Agent
    # -----------------------------

    print("\nRunning Performance Agent...")
    print("-" * 60)

    result = run_performance_agent(context)


    # -----------------------------
    # 5. Display result
    # -----------------------------

    print("\n")
    print("=" * 60)
    print("PERFORMANCE ANALYSIS")
    print("=" * 60)

    print(result)

    print("\n")
    print("=" * 60)
    print("PERFORMANCE AGENT TEST SUCCESSFUL!")
    print("=" * 60)


except Exception as e:

    print("\nPERFORMANCE AGENT TEST FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)