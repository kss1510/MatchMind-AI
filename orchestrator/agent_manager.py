import time
import threading

from agents.strategy.strategy_agent import run_strategy_agent
from agents.opponent.opponent_agent import run_opponent_agent
from agents.team_selection.team_agent import run_team_selection_agent
from agents.performance.performance_agent import run_performance_agent
from agents.fitness.fitness_agent import run_fitness_agent
from agents.report.report_agent import run_report_agent


# Per-agent timeout in seconds.
AGENT_TIMEOUT_SECONDS = 150


def _run_with_timeout(fn, args, timeout):
    """
    Run fn(*args) in a thread. Return (result, elapsed, timed_out).
    """
    result_holder = [None]
    error_holder = [None]

    def target():
        try:
            result_holder[0] = fn(*args)
        except Exception as e:
            error_holder[0] = e

    t = threading.Thread(target=target, daemon=True)
    t0 = time.time()
    t.start()
    t.join(timeout=timeout)
    elapsed = time.time() - t0

    if t.is_alive():
        return None, elapsed, True   # timed out
    if error_holder[0]:
        raise error_holder[0]
    return result_holder[0], elapsed, False


class AgentManager:
    """
    Responsible for executing agents selected by the Planner Agent
    and generating the final MatchMind AI report.
    """

    def __init__(self):

        self.agent_registry = {
            "Strategy Agent":          (run_strategy_agent,          "Strategy Agent"),
            "Opponent Analysis Agent": (run_opponent_agent,           "Opponent Analysis Agent"),
            "Team Selection Agent":    (run_team_selection_agent,     "Team Selection Agent"),
            "Performance Agent":       (run_performance_agent,        "Performance Agent"),
            "Fitness Agent":           (run_fitness_agent,            "Fitness Agent"),
        }

    # ---------------------------------------------------------
    # Execute Selected Agents
    # ---------------------------------------------------------

    def execute_agents(self, selected_agents, match_context):

        results = []

        strategy_report    = ""
        opponent_report    = ""
        team_report        = ""
        performance_report = ""
        fitness_report     = ""

        for agent in selected_agents:

            agent_name = agent["agent"]

            if agent_name not in self.agent_registry:
                continue

            fn, label = self.agent_registry[agent_name]

            print(f"\n[AGENT] Starting: {label} ...")
            t_start = time.time()

            try:
                raw_result, elapsed, timed_out = _run_with_timeout(
                    fn, (match_context,), AGENT_TIMEOUT_SECONDS
                )

                if timed_out:
                    result_text = (
                        f"[TIMEOUT] {label} did not complete within "
                        f"{AGENT_TIMEOUT_SECONDS}s. "
                        f"Insufficient data available for this section."
                    )
                    print(f"[AGENT] {label} TIMED OUT after {elapsed:.0f}s")
                else:
                    result_text = str(raw_result)
                    print(f"[AGENT] {label} completed in {elapsed:.1f}s")

            except Exception as e:
                elapsed = time.time() - t_start
                result_text = (
                    f"[ERROR] {label} failed after {elapsed:.0f}s: {e}. "
                    f"Insufficient data available for this section."
                )
                print(f"[AGENT] {label} FAILED after {elapsed:.0f}s: {e}")

            # Store per-role
            if agent_name == "Strategy Agent":
                strategy_report = result_text
            elif agent_name == "Opponent Analysis Agent":
                opponent_report = result_text
            elif agent_name == "Team Selection Agent":
                team_report = result_text
            elif agent_name == "Performance Agent":
                performance_report = result_text
            elif agent_name == "Fitness Agent":
                fitness_report = result_text

            results.append({
                "agent":  agent_name,
                "result": result_text
            })

        # ---------------------------------------------------------
        # Generate final report regardless of individual failures
        # ---------------------------------------------------------

        print("\n[AGENT] Starting: Report Generator Agent ...")
        t_start = time.time()

        try:
            raw_report, elapsed, timed_out = _run_with_timeout(
                run_report_agent,
                (match_context, performance_report, opponent_report,
                 strategy_report, team_report, fitness_report),
                AGENT_TIMEOUT_SECONDS
            )

            if timed_out:
                final_report = (
                    "[TIMEOUT] Report Agent did not complete within "
                    f"{AGENT_TIMEOUT_SECONDS}s. "
                    "Specialist agent outputs are available above."
                )
                print(f"[AGENT] Report Generator TIMED OUT after {elapsed:.0f}s")
            else:
                final_report = str(raw_report)
                print(f"[AGENT] Report Generator completed in {elapsed:.1f}s")

        except Exception as e:
            elapsed = time.time() - t_start
            final_report = (
                f"[ERROR] Report Generator failed after {elapsed:.0f}s: {e}"
            )
            print(f"[AGENT] Report Generator FAILED: {e}")

        results.append({
            "agent":  "Report Generator Agent",
            "result": final_report
        })

        return results