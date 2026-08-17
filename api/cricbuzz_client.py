import requests

from config.settings import RAPIDAPI_KEY


class CricbuzzClient:
    """
    External API client for Cricbuzz data through RapidAPI.
    """

    BASE_URL = "https://cricbuzz-cricket.p.rapidapi.com"

    HEADERS = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.headers = {
            **self.HEADERS,
            "X-RapidAPI-Key": RAPIDAPI_KEY
        }

    def get_matches(self, category="recent"):
        """
        Fetch available cricket matches.

        category:
            - live
            - recent
            - upcoming
        """

        if category not in ["live", "recent", "upcoming"]:
            raise ValueError(
                "Invalid category. Use live, recent, or upcoming."
            )

        url = f"{self.BASE_URL}/matches/v1/{category}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    def get_scorecard(self, match_id):
        """
        Fetch scorecard information for a cricket match.
        """

        url = f"{self.BASE_URL}/mcenter/v1/{match_id}/hscard"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    def get_match_info(self, match_id):
        """
        Fetch detailed match information from Cricbuzz.
        """

        url = f"{self.BASE_URL}/mcenter/v1/{match_id}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=15
        )

        response.raise_for_status()

        return response.json()