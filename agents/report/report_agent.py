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

MATCH DATE:
{match_context.match_date}

TEAM:
{match_context.team}

OPPONENT:
{match_context.opponent}

FORMAT:
{match_context.format}

VENUE:
{match_context.venue}


============================================================
IMPORTANT DATA RULE
============================================================

The specialist reports below are your PRIMARY SOURCES.

IMPORTANT INSTRUCTIONS:

- Use only statistics contained in the specialist reports
  and MATCH CONTEXT.

- If a statistic is unavailable, explicitly state that it
  is unavailable.

- Do not fabricate player statistics, injuries, form,
  match events, workloads or other unsupported facts.

- Clearly distinguish facts from AI recommendations.

- Always use the MATCH DATE provided above when it is
  available.

- Do not write "Not specified" if the match context
  contains a valid match date.

- Use the exact team, opponent, format and venue provided
  in MATCH CONTEXT.

If a specialist report does not contain enough information,
write:

"Insufficient data available."

Do NOT make up an answer.


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

Synthesize the specialist outputs into ONE concise,
structured match report.

Use EXACTLY this structure:

# MATCHMIND AI — FINAL MATCH REPORT

## 1. Match Overview

Include:

- Team
- Opponent
- Format
- Venue
- Match date

Use the exact values provided in MATCH CONTEXT.


## 2. Executive Summary & Strategy

Synthesize the key findings from the Performance
and Strategy reports.

Focus on meaningful tactical insights.


## 3. Squad & Opponent Insights

Synthesize key findings from the Opponent Analysis
and Team Selection reports.

Mention relevant player or squad insights only when
supported by the provided data.


## 4. Fitness & Workload Assessment

Summarize key findings from the Fitness report.

Do not infer injuries or medical conditions unless
explicitly provided by the data.


## 5. Key Recommendations & Data Limitations

Provide 2-3 practical recommendations.

Clearly mention important missing or limited data.

Recommendations must be based on the available
specialist reports and match context.


============================================================
FINAL INSTRUCTION
============================================================

Keep the response concise and direct.

Do not fabricate statistics.

Do not invent player information.

Do not invent injuries.

Do not invent match events.

Use "Insufficient data available" when required.

Prioritize factual accuracy over speculation.
""",

        expected_output="""
A structured MatchMind AI final cricket report containing:

1. Match Overview
2. Executive Summary & Strategy
3. Squad & Opponent Insights
4. Fitness & Workload Assessment
5. Key Recommendations & Data Limitations

The report must use the exact match context provided
by MatchMind AI and must not fabricate unsupported facts.
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