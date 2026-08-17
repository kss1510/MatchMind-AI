from crewai import Agent, Task, Crew, Process
from config.settings import llm


def create_report_agent():
    """
    Creates the final MatchMind AI Report Agent.
    """

    return Agent(

        role="Senior Cricket Match Report Analyst",

        goal=(
            "Combine the outputs of specialist cricket agents into "
            "one accurate, structured and actionable match report. "
            "Use only the information provided by the specialist agents "
            "and match context."
        ),

        backstory=(
            "You are a senior cricket analyst working with a coaching "
            "and strategy team. Your responsibility is to synthesize "
            "multiple specialist reports into one final decision-support "
            "report. You never invent statistics, player information, "
            "injuries, match results or other unsupported facts."
        ),

        llm=llm,

        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )


def run_report_agent(
    match_context,
    performance_analysis,
    opponent_analysis,
    strategy_analysis,
    team_selection_analysis,
    fitness_analysis
):
    """
    Combines all specialist agent outputs into the final
    MatchMind AI cricket report.
    """

    agent = create_report_agent()

    task = Task(

        description=f"""
You are the FINAL REPORT GENERATOR for MatchMind AI.

Your job is to combine the specialist reports below into ONE
professional cricket analysis report.

============================================================
MATCH CONTEXT
============================================================

{match_context.to_prompt()}


============================================================
IMPORTANT DATA RULE
============================================================

The specialist reports below are your PRIMARY SOURCES.

IMPORTANT INSTRUCTIONS:
- Use only statistics contained in the specialist reports and MATCH CONTEXT.
- If a statistic is unavailable, explicitly state that it is unavailable.
- Do not fabricate player statistics, injuries, form, or match events.
- Clearly distinguish facts (from data) from AI recommendations.

If a specialist report does not contain enough information,
write: "Insufficient data available." Do NOT make up an answer.


============================================================
SPECIALIST REPORT 1 — PERFORMANCE
============================================================

{performance_analysis}


============================================================
SPECIALIST REPORT 2 — OPPONENT
============================================================

{opponent_analysis}


============================================================
SPECIALIST REPORT 3 — STRATEGY
============================================================

{strategy_analysis}


============================================================
SPECIALIST REPORT 4 — TEAM SELECTION
============================================================

{team_selection_analysis}


============================================================
SPECIALIST REPORT 5 — FITNESS
============================================================

{fitness_analysis}


============================================================
FINAL REPORT REQUIREMENTS
============================================================

Synthesize the specialist outputs into ONE concise, structured match report.

Use EXACTLY this structure:

# MATCHMIND AI — FINAL MATCH REPORT

## 1. Match Overview
Include Team, Opponent, Format, Venue, Match date.

## 2. Executive Summary & Strategy
Synthesize key findings from Performance and Strategy reports.

## 3. Squad & Opponent Insights
Synthesize key findings from Opponent Analysis and Team Selection reports.

## 4. Fitness & Workload Assessment
Summarize key findings from the Fitness report.

## 5. Key Recommendations & Data Limitations
Provide 2-3 top recommendations and note any missing data.

============================================================
FINAL INSTRUCTION
============================================================
Keep responses concise and direct. Do not fabricate statistics.
""",

        expected_output="""
A structured MatchMind AI final cricket report containing:
1. Match Overview
2. Executive Summary & Strategy
3. Squad & Opponent Insights
4. Fitness & Workload Assessment
5. Key Recommendations & Data Limitations
""",

        agent=agent
    )

    crew = Crew(

        agents=[agent],

        tasks=[task],

        process=Process.sequential,

        verbose=False,
        max_iter=2,
        max_retry_limit=0
    )

    return crew.kickoff()