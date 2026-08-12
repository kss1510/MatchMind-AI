from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import parse_scorecard

print("=" * 60)
print("CRICBUZZ SCORECARD PARSER TEST")
print("=" * 60)

client = CricbuzzClient()

print("\nFetching scorecard...")

match_id = 40381

data = client.get_scorecard(match_id)

print("\nAPI call successful!")

parsed = parse_scorecard(data)

print("\nParsed Scorecard:")

for innings in parsed["innings"]:

    print("\n----------------------------------------")
    print("Innings ID:", innings["innings_id"])

    print("\nTotal:")
    print(innings["total"])

    print("\nBatting:")
    for player in innings["batting"]:
        print(player)

    print("\nBowling:")
    for player in innings["bowling"]:
        print(player)

    print("\nExtras:")
    print(innings["extras"])

print("\n" + "=" * 60)
print("SCORECARD PARSER TEST COMPLETED")
print("=" * 60)