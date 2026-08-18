# 🏏 MatchMind AI

## Multi-Agent Cricket Intelligence Platform

MatchMind AI is a multi-agent cricket intelligence platform that combines live cricket match data with specialized AI agents to generate structured and actionable match analysis.

The system retrieves match and scorecard information through the Cricbuzz API, converts it into structured match context, executes multiple specialist agents, and synthesizes their outputs through a dedicated Report Generator Agent.

## 🚀 Features

- 🏏 Cricket match and scorecard data retrieval
- 🤖 Multi-agent cricket analysis
- 📊 Batting and bowling performance analysis
- 🎯 Tactical strategy analysis
- 🔍 Opponent analysis
- 👥 Team-selection insights
- 💪 Fitness and workload assessment
- 🧠 AI-generated final match report
- ⏱️ Agent timeout protection
- 🌐 Streamlit interactive interface
- 📋 Structured scorecard visualization

## 🧠 Multi-Agent Architecture

MatchMind AI uses five specialist agents followed by a dedicated Report Generator Agent.

### Specialist Agents

1. **Strategy Agent** — tactical and strategic analysis
2. **Opponent Analysis Agent** — opponent strengths and weaknesses
3. **Team Selection Agent** — squad and player-selection insights
4. **Performance Agent** — batting and bowling performance
5. **Fitness Agent** — workload and fitness-related assessment

### Report Generator Agent

The Report Generator Agent receives the outputs of all specialist agents and synthesizes them into one structured final report.

The final report contains:

1. Match Overview
2. Executive Summary & Strategy
3. Squad & Opponent Insights
4. Fitness & Workload Assessment
5. Key Recommendations & Data Limitations

## 🏗️ Architecture

```text
Streamlit UI
      │
      ▼
MatchMind Engine
      │
      ▼
Cricbuzz API Client
      │
      ▼
Cricbuzz Parser
      │
      ▼
Structured Match Context
      │
      ▼
Agent Manager / Orchestrator
      │
      ├── Strategy Agent
      ├── Opponent Analysis Agent
      ├── Team Selection Agent
      ├── Performance Agent
      └── Fitness Agent
                │
                ▼
       Report Generator Agent
                │
                ▼
      Final MatchMind AI Report

Detailed architecture documentation is available in docs/architecture.md.

🔄 Analysis Pipeline
User selects a cricket match from the Streamlit interface.
MatchMind retrieves match and scorecard data through the Cricbuzz API.
The parser converts the API response into structured match context.
The Planner/Orchestrator determines the specialist agents required for analysis.
Specialist agents execute independently on the shared match context.
Agent results are collected by the Agent Manager.
The Report Generator Agent synthesizes the available specialist outputs.
The final report is displayed in the Streamlit interface.
🛡️ Reliability

Each agent execution is protected by a 300-second timeout.

If an individual agent times out or fails, the orchestrator records the issue and continues the workflow. The final report can therefore be generated using the specialist outputs that completed successfully.

The Report Generator also follows a strict data-grounding policy. Unsupported statistics, player information, injuries, workloads, or match events should not be fabricated.

🧰 Technology Stack
Python
Streamlit — interactive web interface
CrewAI — multi-agent orchestration
RapidAPI / Cricbuzz API — cricket match data
Requests — API communication
python-dotenv — environment configuration
Git / GitHub — version control
📁 Project Structure
MatchMind-AI/
│
├── agents/
│   ├── strategy/
│   ├── opponent/
│   ├── team_selection/
│   ├── performance/
│   ├── fitness/
│   └── report/
│
├── api/
│   ├── cricbuzz_client.py
│   └── cricbuzz_parser.py
│
├── config/
│   ├── agents_config.py
│   ├── match_context.py
│   ├── prompts.py
│   └── settings.py
│
├── core/
│   └── matchmind_engine.py
│
├── data/
│   ├── cricket/
│   └── football/
│
├── docs/
│   ├── architecture.md
│   ├── presentation/
│   ├── proposal/
│   └── screenshots/
│
├── orchestrator/
│   └── agent_manager.py
│
├── tests/
│   ├── test_cricbuzz.py
│   ├── test_cricbuzz_parser.py
│   ├── test_end_to_end.py
│   ├── test_fitness_agent.py
│   ├── test_manager.py
│   ├── test_match_context.py
│   ├── test_match_info.py
│   ├── test_match_info_parser.py
│   ├── test_matchmind_engine.py
│   ├── test_opponent_agent.py
│   ├── test_performance_agent.py
│   ├── test_report_agent.py
│   ├── test_scorecard_parser.py
│   ├── test_strategy_agent.py
│   └── test_team_selection_agent.py
│
├── ui/
│   └── app.py
│
├── utils/
│
├── .env.example
├── .gitignore
├── LICENSE
├── main.py
├── requirements.txt
└── README.md

.env, virtual environments, caches, and other local configuration files should not be committed to GitHub.

▶️ Running the Application
1. Clone the repository
git clone https://github.com/kss1510/MatchMind-AI.git
cd MatchMind-AI
2. Create and activate a virtual environment

Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file and add the required API credentials.

Example:

RAPIDAPI_KEY=your_rapidapi_key

Add any LLM/API credentials required by config/settings.py.

5. Run MatchMind AI
streamlit run ui/app.py

The application will open in the browser with the MatchMind AI interface.

📊 Final Report

The generated report is designed as a decision-support output rather than a replacement for professional cricket coaching judgment.

Recommendations are based on the data retrieved for the selected match and the outputs of the specialist agents.

The final report includes:

Match overview
Performance and strategy analysis
Squad and opponent insights
Fitness and workload assessment
Key recommendations
Data limitations
🎯 Project Goal

MatchMind AI demonstrates how multiple specialized AI agents can collaborate on a single domain-specific problem.

Instead of relying on one general-purpose agent, the system separates cricket analysis into focused roles and uses a dedicated reporting agent to synthesize their findings into a coherent final result.

🔬 Testing

The project includes automated tests covering major components of the system, including:

Cricbuzz API integration
Cricbuzz response parsing
Match context
Match information parsing
MatchMind engine
Specialist agents
Agent manager
Report generation
End-to-end workflow

Run the test suite with:

pytest
⚙️ Agent Execution

The orchestrator executes the selected specialist agents and collects their outputs before invoking the Report Generator Agent.

Each specialist agent has an execution timeout of 300 seconds to prevent the application from becoming indefinitely blocked by a slow model response.

The final report generation also uses the available specialist outputs and match context.

📌 Data & AI Safety

MatchMind AI follows a data-grounded analysis approach.

The agents are instructed to:

Use available match data as their primary source.
Avoid fabricating statistics or player information.
Explicitly identify unavailable information.
Distinguish factual observations from AI-generated recommendations.
Treat the final output as decision support rather than absolute prediction.
🎓 Project Context

MatchMind AI was developed as an academic multi-agent AI project focused on demonstrating practical agent orchestration, domain-specific reasoning, API integration, structured data processing, and AI-generated decision support.

📄 License

This project is developed for educational and academic purposes.
