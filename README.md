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
