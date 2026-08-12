from config.match_context import MatchContext
from agents.team_selection.team_agent import run_team_selection_agent


print("=" * 60)
print("MATCHMIND AI - TEAM SELECTION AGENT TEST")
print("=" * 60)

try:

    context = MatchContext(
        team="India",
        opponent="England",
        format="T20",
        venue="Wankhede Stadium",
        match_date="10 August 2026"
    )

    print("\nMatch context created successfully!")

    print("\nRunning Team Selection Agent...")
    print("-" * 60)

    result = run_team_selection_agent(context)

    print("\n")
    print("=" * 60)
    print("TEAM SELECTION ANALYSIS")
    print("=" * 60)

    print(result)

    print("\n")
    print("=" * 60)
    print("TEAM SELECTION AGENT TEST SUCCESSFUL!")
    print("=" * 60)

except Exception as e:

    print("\nTEAM SELECTION AGENT TEST FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)