from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser


print("=" * 60)
print("CRICBUZZ PARSER TEST")
print("=" * 60)


try:

    # Get raw data from Cricbuzz
    client = CricbuzzClient()

    # Use the same match ID that worked in test_cricbuzz.py
    data = client.get_scorecard(40381)

    print("\nAPI call successful!")

    # Parse the response
    parsed = CricbuzzParser.parse_scorecard(data)

    print("\nParsed Match Data:")
    print(parsed)

    print("\nParser working successfully!")

except Exception as e:

    print("\nParser test failed!")
    print(type(e).__name__)
    print(e)