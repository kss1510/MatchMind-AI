from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser
from config.match_context import MatchContext
from agents.opponent.opponent_agent import run_opponent_agent


MATCH_ID = 40381


print("=" * 60)
print("MATCHMIND AI - OPPONENT AGENT TEST")
print("=" * 60)


try:

    client = CricbuzzClient()

    scorecard_raw = client.get_scorecard(MATCH_ID)

    print("\nAPI call successful!")

    parsed_scorecard = CricbuzzParser.parse_scorecard(scorecard_raw)

    print("Scorecard parsed successfully!")

    context = MatchContext(
        team="India",
        opponent="England",
        format="T20",
        venue="Wankhede Stadium",
        match_date="10 August 2026"
    )

    print("Match context created successfully!")

    print("\nRunning Opponent Agent...")
    print("-" * 60)

    result = run_opponent_agent(context)

    print("\n")
    print("=" * 60)
    print("OPPONENT ANALYSIS")
    print("=" * 60)

    print(result)

    print("\n")
    print("=" * 60)
    print("OPPONENT AGENT TEST SUCCESSFUL!")
    print("=" * 60)


except Exception as e:

    print("\nOPPONENT AGENT TEST FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)