# MatchMind AI — System Architecture

## Architecture Overview

MatchMind AI follows a modular multi-agent architecture for cricket
match intelligence.

The system retrieves match and scorecard information through the
Cricbuzz API, parses the data into a structured match context, and
passes the context through multiple specialist AI agents. Their outputs
are then synthesized by a dedicated Report Generator Agent.

```mermaid
flowchart TD

    A["User"] --> B["Streamlit UI"]

    B --> C["MatchMind Engine"]

    C --> D["Cricbuzz API Client"]
    D --> E["Cricbuzz / RapidAPI"]

    E --> F["Cricbuzz Parser"]

    F --> G["Structured Match Context"]

    G --> H["Agent Manager / Orchestrator"]

    H --> I["Strategy Agent"]
    H --> J["Opponent Analysis Agent"]
    H --> K["Team Selection Agent"]
    H --> L["Performance Agent"]
    H --> M["Fitness Agent"]

    I --> N["Specialist Agent Outputs"]
    J --> N
    K --> N
    L --> N
    M --> N

    N --> O["Report Generator Agent"]

    O --> P["Final MatchMind AI Report"]

    P --> B