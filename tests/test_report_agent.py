from config.match_context import MatchContext
from agents.strategy.report.report_agent import run_report_agent


print("=" * 60)
print("MATCHMIND AI - REPORT AGENT TEST")
print("=" * 60)


try:

    # -----------------------------
    # 1. Create Match Context
    # -----------------------------

    context = MatchContext(
        team="India",
        opponent="England",
        format="T20",
        venue="Wankhede Stadium",
        match_date="10 August 2026"
    )

    print("\nMatch context created successfully!")


    # -----------------------------
    # 2. Sample Agent Outputs
    # -----------------------------

    performance_analysis = """
    India has a strong batting unit with good scoring ability.
    The available information does not contain complete recent
    performance statistics, so detailed statistical conclusions
    should be treated cautiously.
    """

    opponent_analysis = """
    England has a strong batting lineup and should be treated as
    a significant threat. Detailed opponent statistics are not
    fully available in the current context.
    """

    strategy_analysis = """
    India should maintain an aggressive powerplay approach,
    rotate strike during the middle overs and use specialist
    bowlers strategically during the death overs.
    """

    team_selection_analysis = """
    The team should maintain a balanced combination of batters,
    bowlers and all-rounders. Final player selection should depend
    on actual player availability and performance data.
    """

    fitness_analysis = """
    Detailed player fitness information is unavailable.
    Workload and availability should therefore be checked before
    final team selection.
    """


    # -----------------------------
    # 3. Run Report Agent
    # -----------------------------

    print("\nRunning Report Agent...")
    print("-" * 60)

    result = run_report_agent(
        context,
        performance_analysis,
        opponent_analysis,
        strategy_analysis,
        team_selection_analysis,
        fitness_analysis
    )


    # -----------------------------
    # 4. Display Final Report
    # -----------------------------

    print("\n")
    print("=" * 60)
    print("FINAL MATCHMIND AI REPORT")
    print("=" * 60)

    print(result)

    print("\n")
    print("=" * 60)
    print("REPORT AGENT TEST SUCCESSFUL!")
    print("=" * 60)


except Exception as e:

    print("\nREPORT AGENT TEST FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)