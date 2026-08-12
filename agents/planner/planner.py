from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM

from config.settings import (
    llm,
    VERBOSE,
)

# ============================================================
# PLANNER AGENT
# ============================================================

planner_agent = Agent(
    role="Planner Agent",

    goal=(
        "Analyze the user's cricket analysis request and select "
        "the most appropriate MatchMind AI specialist agents."
    ),

    backstory=(
        "You are the coordinator of MatchMind AI. "
        "You never perform cricket analysis yourself. "
        "You decide which specialist agents are required "
        "to answer the user's request."
    ),

    llm=llm,

    verbose=VERBOSE,
    max_iter=2,
    max_retry_limit=0
)


# ============================================================
# AVAILABLE SPECIALIST AGENTS
# ============================================================

AVAILABLE_AGENTS = [
    "Strategy Agent",
    "Opponent Analysis Agent",
    "Team Selection Agent",
    "Performance Agent",
    "Fitness Agent"
]


# ============================================================
# PLANNER FUNCTION
# ============================================================

def plan_agents(user_request):
    """
    Ask the Planner Agent to select the specialist agents
    required for the user's cricket analysis request.

    Returns:
        List of dictionaries containing agent names and reasons.
    """

    task = Task(

        description=f"""
        You are the planning component of MatchMind AI.

        User Request:
        {user_request}

        Available specialist agents:

        1. Strategy Agent
           - Match tactics
           - Batting/bowling strategy
           - Tactical recommendations

        2. Opponent Analysis Agent
           - Opponent strengths
           - Opponent weaknesses
           - Threat analysis

        3. Team Selection Agent
           - Playing XI
           - Player combinations
           - Role-based selection

        4. Performance Agent
           - Batting performance
           - Bowling performance
           - Team performance
           - Strengths and weaknesses

        5. Fitness Agent
           - Fitness considerations
           - Workload
           - Player availability
           - Fitness-related recommendations

        Select ONLY the agents that are relevant to the
        user's request.

        If the request is a general complete match analysis,
        select all five agents.

        Return ONLY the names of the selected agents,
        one per line.

        Use the exact agent names:

        Strategy Agent
        Opponent Analysis Agent
        Team Selection Agent
        Performance Agent
        Fitness Agent
        """,

        expected_output="""
        A list containing only the names of the selected
        specialist agents, one agent per line.
        """,

        agent=planner_agent
    )


    crew = Crew(
        agents=[planner_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=VERBOSE
    )


    result = crew.kickoff()

    result_text = str(result)


    # ========================================================
    # Extract valid agent names
    # ========================================================

    selected_agents = []

    for agent_name in AVAILABLE_AGENTS:

        if agent_name.lower() in result_text.lower():

            selected_agents.append(
                {
                    "agent": agent_name,
                    "reason": "Selected by Planner Agent"
                }
            )


    # ========================================================
    # Safety fallback
    # ========================================================

    if not selected_agents:

        selected_agents = [
            {
                "agent": agent_name,
                "reason": "General match analysis"
            }

            for agent_name in AVAILABLE_AGENTS
        ]


    return selected_agents