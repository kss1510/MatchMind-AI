class CricbuzzParser:
    """
    Converts raw Cricbuzz API responses into clean,
    structured cricket match information.
    """

    @staticmethod
    def parse_scorecard(data):
        """
        Parse the scorecard returned by CricbuzzClient.
        """

        scorecard = data.get("scorecard", [])

        parsed = {
            "innings": []
        }

        for innings in scorecard:

            innings_data = {
                "innings_id": innings.get("inningsid"),
                "batting": []
            }

            batsmen = innings.get("batsman", [])

            for batsman in batsmen:

                player = {
                    "name": batsman.get("name"),
                    "runs": batsman.get("runs"),
                    "balls": batsman.get("balls"),
                    "fours": batsman.get("fours"),
                    "sixes": batsman.get("sixes"),
                    "strike_rate": batsman.get("strkrate"),
                    "out": batsman.get("outdesc")
                }

                innings_data["batting"].append(player)

            parsed["innings"].append(innings_data)

        return parsed


def parse_scorecard(data):
    """
    Module-level wrapper for scorecard parsing.
    """

    return CricbuzzParser.parse_scorecard(data)


def parse_match_info(data):
    """
    Parse raw Cricbuzz match information into a clean structure.
    """

    team1 = data.get("team1", {})
    team2 = data.get("team2", {})
    venue_info = data.get("venueinfo", {})

    return {
        "match_id": data.get("matchid"),
        "series": data.get("seriesname"),
        "match_description": data.get("matchdesc"),
        "format": data.get("matchformat"),
        "start_date": data.get("startdate"),
        "end_date": data.get("enddate"),
        "status": data.get("status"),
        "short_status": data.get("shortstatus"),

        "team1": team1.get("teamname"),
        "team2": team2.get("teamname"),

        "venue": venue_info.get("ground"),
        "city": venue_info.get("city"),
        "country": venue_info.get("country")
    }