import streamlit as st
import sys
import os

# Add project root to sys.path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from core.matchmind_engine import MatchMindEngine
from api.cricbuzz_client import CricbuzzClient


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MatchMind AI",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM UI STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Hero title */
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #a9adb7;
        margin-bottom: 1.5rem;
    }

    /* Section titles */
    .section-title {
        font-size: 1.65rem;
        font-weight: 700;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    /* Information cards */
    .info-card {
        background: #171920;
        border: 1px solid #30333d;
        border-radius: 12px;
        padding: 18px;
        min-height: 105px;
    }

    .info-label {
        color: #9da1ad;
        font-size: 0.85rem;
        margin-bottom: 6px;
    }

    .info-value {
        font-size: 1.05rem;
        font-weight: 600;
    }

    /* Agent status */
    .agent-card {
        background: #171920;
        border: 1px solid #30333d;
        border-radius: 10px;
        padding: 14px 16px;
        margin-bottom: 10px;
    }

    .agent-success {
        color: #4ade80;
        font-weight: 600;
    }

    /* Recommendation box */
    .recommendation-box {
        background: #171920;
        border-left: 4px solid #ff4b4b;
        padding: 16px 18px;
        border-radius: 8px;
        margin-top: 10px;
    }

    /* Small muted text */
    .muted {
        color: #9da1ad;
    }

    /* Divider */
    hr {
        border-color: #30333d;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def extract_matches(data):
    """
    Convert Cricbuzz's nested match response into a simple
    list of match dictionaries for the UI.
    """

    matches = []

    for type_match in data.get("typeMatches", []):

        for series_match in type_match.get("seriesMatches", []):

            series_wrapper = series_match.get(
                "seriesAdWrapper",
                {}
            )

            series_name = series_wrapper.get(
                "seriesName",
                "Cricket Match"
            )

            for match in series_wrapper.get("matches", []):

                match_info = match.get(
                    "matchInfo",
                    {}
                )

                team1 = match_info.get(
                    "team1",
                    {}
                )

                team2 = match_info.get(
                    "team2",
                    {}
                )

                match_id = match_info.get(
                    "matchId"
                )

                if not match_id:
                    continue

                matches.append(
                    {
                        "match_id": match_id,

                        "team1": team1.get(
                            "teamName",
                            "Team 1"
                        ),

                        "team2": team2.get(
                            "teamName",
                            "Team 2"
                        ),

                        "team1_short": team1.get(
                            "teamSName",
                            ""
                        ),

                        "team2_short": team2.get(
                            "teamSName",
                            ""
                        ),

                        "match_desc": match_info.get(
                            "matchDesc",
                            ""
                        ),

                        "format": match_info.get(
                            "matchFormat",
                            ""
                        ),

                        "series": series_name,

                        "state": match_info.get(
                            "state",
                            ""
                        ),

                        "status": match_info.get(
                            "status",
                            ""
                        ),

                        "venue": match_info.get(
                            "venueInfo",
                            {}
                        ).get(
                            "ground",
                            ""
                        )
                    }
                )

    return matches


@st.cache_data(ttl=300)
def fetch_matches(category):
    """
    Fetch matches from Cricbuzz.

    Cached for 5 minutes to avoid repeated API calls
    whenever Streamlit reruns the application.
    """

    client = CricbuzzClient()

    data = client.get_matches(category)

    return extract_matches(data)


def format_match(match):
    """
    Create a clean label for the match selector.
    """

    return (
        f"{match['team1']} vs {match['team2']} "
        f"— {match['match_desc']} "
        f"({match['format']})"
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

def main():

    # --------------------------------------------------------
    # HERO SECTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="hero-title">MatchMind AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-subtitle">'
        'Multi-Agent Cricket Intelligence Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")


    # --------------------------------------------------------
    # MATCH SELECTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">🏏 Select Match</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(
        [1, 2],
        gap="large"
    )

    with col1:

        category = st.selectbox(
            "Match Category",
            [
                "Recent Matches",
                "Live Matches",
                "Upcoming Matches"
            ]
        )

    category_map = {
        "Recent Matches": "recent",
        "Live Matches": "live",
        "Upcoming Matches": "upcoming"
    }

    api_category = category_map[category]


    # --------------------------------------------------------
    # FETCH MATCHES
    # --------------------------------------------------------

    try:

        with st.spinner(
            f"Loading {category.lower()}..."
        ):

            matches = fetch_matches(
                api_category
            )

    except Exception as e:

        st.error(
            f"Unable to fetch matches: {str(e)}"
        )

        return


    if not matches:

        st.warning(
            "No matches are currently available."
        )

        return


    # --------------------------------------------------------
    # MATCH OPTIONS
    # --------------------------------------------------------

    match_options = [
        format_match(match)
        for match in matches
    ]

    with col2:

        selected_label = st.selectbox(
            "Select Match",
            match_options
        )


    selected_index = match_options.index(
        selected_label
    )

    selected_match = matches[
        selected_index
    ]


    # --------------------------------------------------------
    # MATCH DETAILS
    # --------------------------------------------------------

    st.markdown("---")

    st.markdown(
        '<div class="section-title">📋 Match Details</div>',
        unsafe_allow_html=True
    )

    detail_col1, detail_col2, detail_col3 = st.columns(
        3,
        gap="medium"
    )


    with detail_col1:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">TEAMS</div>
                <div class="info-value">
                    {selected_match['team1']}
                    <br>
                    vs
                    <br>
                    {selected_match['team2']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with detail_col2:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">FORMAT</div>
                <div class="info-value">
                    {selected_match['format']}
                </div>
                <div class="muted">
                    {selected_match['match_desc']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with detail_col3:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">STATUS</div>
                <div class="info-value">
                    {selected_match['state']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.markdown("")


    if selected_match["series"]:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">SERIES</div>
                <div class="info-value">
                    {selected_match['series']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    if selected_match["venue"]:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-label">VENUE</div>
                <div class="info-value">
                    {selected_match['venue']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # --------------------------------------------------------
    # ANALYZE BUTTON
    # --------------------------------------------------------

    st.markdown("")

    analyze_btn = st.button(
        "🔍 Analyze Match",
        type="primary",
        use_container_width=False
    )


    if not analyze_btn:
        return


    # --------------------------------------------------------
    # UPCOMING MATCH PROTECTION
    # --------------------------------------------------------

    if api_category == "upcoming":

        st.warning(
            "Upcoming matches cannot be analyzed yet. "
            "Please select a live or recent completed match."
        )

        return


    match_id = selected_match["match_id"]


    st.markdown("---")


    # --------------------------------------------------------
    # INITIALIZE ENGINE
    # --------------------------------------------------------

    with st.spinner(
        "Initializing MatchMind AI Engine..."
    ):

        engine = MatchMindEngine()


    # --------------------------------------------------------
    # PROCESS MATCH
    # --------------------------------------------------------

    with st.spinner(
        "Fetching scorecard, parsing match data, "
        "and running specialist agents "
        "(this may take a few minutes)..."
    ):

        result = engine.process_match(
            int(match_id)
        )


    # --------------------------------------------------------
    # HANDLE FAILURE
    # --------------------------------------------------------

    if not result.get("success"):

        st.error(
            f"Execution Failed: "
            f"{result.get('error')}"
        )

        return


    # --------------------------------------------------------
    # SUCCESS
    # --------------------------------------------------------

    st.success(
        "Match analysis completed successfully!"
    )

    match_context = result[
        "match_context"
    ]


    # ========================================================
    # MATCH OVERVIEW
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Match Overview</div>',
        unsafe_allow_html=True
    )

    overview_col1, overview_col2, overview_col3, overview_col4 = st.columns(
        4,
        gap="medium"
    )


    with overview_col1:

        st.metric(
            "Teams",
            f"{match_context.team} vs "
            f"{match_context.opponent}"
        )


    with overview_col2:

        st.metric(
            "Format",
            match_context.format
        )


    with overview_col3:

        st.metric(
            "Venue",
            match_context.venue
        )


    with overview_col4:

        st.metric(
            "Match Date",
            str(match_context.match_date)
        )


    # ========================================================
    # SCORECARD
    # ========================================================

    with st.expander(
        "📋 View Scorecard",
        expanded=False
    ):

        innings_list = (
            match_context.scorecard.get(
                "innings",
                []
            )
        )


        if not innings_list:

            st.info(
                "No scorecard data available."
            )


        for i, innings in enumerate(
            innings_list
        ):

            total = innings.get(
                "total",
                {}
            )

            runs = total.get(
                "runs",
                "?"
            )

            wickets = total.get(
                "wickets",
                "?"
            )

            overs = total.get(
                "overs",
                "?"
            )

            run_rate = total.get(
                "run_rate",
                "?"
            )


            st.markdown(
                f"### Innings {i + 1}"
            )


            score_col1, score_col2, score_col3, score_col4 = st.columns(
                4
            )


            with score_col1:

                st.metric(
                    "Score",
                    f"{runs}/{wickets}"
                )


            with score_col2:

                st.metric(
                    "Overs",
                    str(overs)
                )


            with score_col3:

                st.metric(
                    "Run Rate",
                    str(run_rate)
                )


            with score_col4:

                batting_count = len(
                    [
                        b
                        for b in innings.get(
                            "batting",
                            []
                        )
                        if b.get("name")
                    ]
                )

                st.metric(
                    "Batters",
                    batting_count
                )


            batting = [
                b
                for b in innings.get(
                    "batting",
                    []
                )
                if b.get("name")
            ]


            if batting:

                st.markdown("#### 🏏 Batting")

                st.dataframe(
                    batting,
                    hide_index=True,
                    width="stretch"
                )


            bowling = [
                b
                for b in innings.get(
                    "bowling",
                    []
                )
                if b.get("name")
            ]


            if bowling:

                st.markdown("#### 🎯 Bowling")

                st.dataframe(
                    bowling,
                    hide_index=True,
                    width="stretch"
                )


            if i < len(innings_list) - 1:

                st.markdown("---")


    # ========================================================
    # AGENT EXECUTION STATUS
    # ========================================================

    with st.expander(
        "🤖 View Agent Execution Status",
        expanded=False
    ):

        selected_agents = [
            agent["agent"]
            for agent in result[
                "selected_agents"
            ]
        ]


        st.write(
            "**Selected Specialist Agents:**"
        )


        agent_columns = st.columns(
            3,
            gap="medium"
        )


        specialist_results = [
            res
            for res in result[
                "agent_results"
            ]
            if res["agent"]
            != "Report Generator Agent"
        ]


        for index, res in enumerate(
            specialist_results
        ):

            with agent_columns[
                index % 3
            ]:

                st.markdown(
                    f"""
                    <div class="agent-card">
                        <div class="agent-success">
                            ✅ {res['agent']}
                        </div>
                        <div class="muted">
                            Analysis completed
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        st.caption(
            " | ".join(selected_agents)
        )


    # ========================================================
    # FINAL REPORT
    # ========================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">'
        '🧠 Final MatchMind AI Report'
        '</div>',
        unsafe_allow_html=True
    )


    final_report = result.get(
        "final_report",
        ""
    )


    if not final_report:

        st.warning(
            "The final report was not generated."
        )

    elif final_report.startswith(
        "[TIMEOUT]"
    ):

        st.warning(
            final_report
        )

        st.info(
            "The specialist agent analyses are still "
            "available above."
        )

    else:

        st.markdown(
            final_report
        )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.markdown("---")

    st.caption(
        "MatchMind AI • Multi-Agent Cricket Intelligence "
        "Platform"
    )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()