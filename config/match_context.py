class MatchContext:
    """
    Stores information about the match being analyzed.
    """

    def __init__(
        self,
        team,
        opponent,
        format,
        venue=None,
        match_date=None,
        match_status=None,
        series=None
    ):
        self.team = team
        self.opponent = opponent
        self.format = format
        self.venue = venue
        self.match_date = match_date
        self.match_status = match_status
        self.series = series

    def to_prompt(self):

        return f"""
Match Context:

Team: {self.team}
Opponent: {self.opponent}
Format: {self.format}
Venue: {self.venue}
Match Date: {self.match_date}
Series: {self.series}
Match Status: {self.match_status}
"""