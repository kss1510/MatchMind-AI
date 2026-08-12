from config.match_context import MatchContext
from agents.strategy.strategy_agent import run_strategy_agent


print("=" * 60)
print("MATCHMIND AI - STRATEGY AGENT TEST")
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

    print("\nRunning Strategy Agent...")
    print("-" * 60)

    result = run_strategy_agent(context)

    print("\n")
    print("=" * 60)
    print("STRATEGY ANALYSIS")
    print("=" * 60)

    print(result)

    print("\n")
    print("=" * 60)
    print("STRATEGY AGENT TEST SUCCESSFUL!")
    print("=" * 60)

except Exception as e:

    print("\nSTRATEGY AGENT TEST FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)