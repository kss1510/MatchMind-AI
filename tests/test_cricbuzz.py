from api.cricbuzz_client import CricbuzzClient


client = CricbuzzClient()

# Test match ID from the RapidAPI example
match_id = "40381"

print("\n" + "=" * 60)
print("CRICBUZZ API TEST")
print("=" * 60)

try:
    scorecard = client.get_scorecard(match_id)

    print("\nAPI call successful!")
    print("\nResponse type:")
    print(type(scorecard))

    print("\nResponse:")
    print(scorecard)

except Exception as e:
    print("\nAPI call failed!")
    print(type(e).__name__)
    print(e)