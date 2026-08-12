import json

class MatchContext:
    """
    Centralized context shared across all MatchMind AI agents.
    """

    def __init__(
        self,
        team,
        opponent,
        format,
        venue,
        match_date,
        match_data=None,
        scorecard=None
    ):

        self.team = team
        self.opponent = opponent
        self.format = format
        self.venue = venue
        self.match_date = match_date

        self.match_data = match_data or {}
        self.scorecard = scorecard or {}

    def to_prompt(self):
        """
        Returns a lean, human-readable match summary for LLM consumption.
        Avoids dumping raw JSON to keep prompt size small and inference fast.
        """
        lines = [
            "MATCH CONTEXT",
            f"Teams: {self.team} vs {self.opponent}",
            f"Format: {self.format}",
            f"Venue: {self.venue}",
        ]

        # Match info summary
        md = self.match_data
        if md:
            lines.append(f"Series: {md.get('series', 'N/A')}")
            lines.append(f"Status: {md.get('status', 'N/A')}")

        # Scorecard summary - one section per innings
        sc = self.scorecard
        innings_list = sc.get("innings", [])
        if innings_list:
            lines.append("")
            lines.append("SCORECARD SUMMARY")
            for i, inns in enumerate(innings_list):
                total = inns.get("total", {})
                lines.append(
                    f"Innings {i+1}: "
                    f"{total.get('runs', '?')}/{total.get('wickets', '?')} "
                    f"in {total.get('overs', '?')} overs "
                    f"(RR: {total.get('run_rate', '?')})"
                )
                # Top batsmen (max 5)
                batting = inns.get("batting", [])
                if batting:
                    lines.append("  Batting:")
                    for b in batting[:5]:
                        lines.append(
                            f"    {b.get('name')}: "
                            f"{b.get('runs')} ({b.get('balls')} balls) "
                            f"SR:{b.get('strike_rate')}"
                        )
                # Top bowlers (max 4)
                bowling = inns.get("bowling", [])
                if bowling:
                    lines.append("  Bowling:")
                    for bw in bowling[:4]:
                        lines.append(
                            f"    {bw.get('name')}: "
                            f"{bw.get('wickets')}/{bw.get('runs')} "
                            f"({bw.get('overs')} ov) "
                            f"Eco:{bw.get('economy')}"
                        )
        else:
            lines.append("Scorecard: Not available.")

        lines.append("")
        lines.append("INSTRUCTIONS: Use ONLY the data above. Do not fabricate statistics.")

        return "\n".join(lines)