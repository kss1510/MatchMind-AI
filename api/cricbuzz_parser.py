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
                "batting": [],
                "bowling": [],
                "extras": {},
                "total": {}
            }

            # -------------------------------------------------
            # BATTING
            # -------------------------------------------------

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

            # -------------------------------------------------
            # BOWLING
            # -------------------------------------------------

            bowlers = innings.get("bowler", [])

            for bowler in bowlers:

                player = {
                    "name": bowler.get("name"),
                    "overs": bowler.get("overs"),
                    "maidens": bowler.get("maidens"),
                    "runs": bowler.get("runs"),
                    "wickets": bowler.get("wickets"),
                    "economy": bowler.get("economy")
                }

                innings_data["bowling"].append(player)

            # -------------------------------------------------
            # EXTRAS
            # -------------------------------------------------

            extras = innings.get("extras", {})

            innings_data["extras"] = {
                "wides": extras.get("wides"),
                "noballs": extras.get("noballs"),
                "byes": extras.get("byes"),
                "legbyes": extras.get("legbyes"),
                "penalty": extras.get("penalty"),
                "total": extras.get("total")
            }

            # -------------------------------------------------
            # INNINGS TOTAL
            # -------------------------------------------------

            innings_data["total"] = {
                "runs": innings.get("score"),
                "wickets": innings.get("wickets"),
                "overs": innings.get("overs"),
                "run_rate": innings.get("runrate")
            }

            parsed["innings"].append(innings_data)

        return parsed

    # ---------------------------------------------------------
    # MATCH INFORMATION
    # ---------------------------------------------------------

    @staticmethod
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


# ---------------------------------------------------------
# Module-level wrapper functions
# ---------------------------------------------------------

def parse_scorecard(data):
    """
    Module-level wrapper for CricbuzzParser.parse_scorecard().
    """
    return CricbuzzParser.parse_scorecard(data)


def parse_match_info(data):
    """
    Module-level wrapper for CricbuzzParser.parse_match_info().
    """
    return CricbuzzParser.parse_match_info(data)