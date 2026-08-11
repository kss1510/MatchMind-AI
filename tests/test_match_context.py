from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import CricbuzzParser
from config.match_context import MatchContext


print("=" * 60)
print("MATCH CONTEXT INTEGRATION TEST")
print("=" * 60)


try:
    # 1. Call Cricbuzz API
    client = CricbuzzClient()

    data = client.get_scorecard(40381)

    print("\nAPI call successful!")

    # 2. Parse API response
    parsed_data = CricbuzzParser.parse_scorecard(data)

    print("Parser successful!")

    # 3. Create MatchContext using parsed data
    match_context = MatchContext(
        team="India",
        opponent="England",
        format="T20",
        venue="Wankhede Stadium",
        match_date="10 August 2026",
        match_data=parsed_data
    )

    print("\nMatchContext created successfully!")

    # 4. Generate agent prompt
    prompt = match_context.to_prompt()

    print("\n" + "=" * 60)
    print("GENERATED MATCH CONTEXT")
    print("=" * 60)

    print(prompt)

    print("\n" + "=" * 60)
    print("MATCH CONTEXT TEST SUCCESSFUL!")
    print("=" * 60)


except Exception as e:

    print("\nMATCH CONTEXT TEST FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)