from api.cricbuzz_client import CricbuzzClient


print("=" * 60)
print("CRICBUZZ MATCH INFO TEST")
print("=" * 60)


try:

    client = CricbuzzClient()

    match_info = client.get_match_info(40381)

    print("\nAPI call successful!")

    print("\nResponse type:")
    print(type(match_info))

    print("\nMatch Information:")
    print(match_info)


except Exception as e:

    print("\nMATCH INFO API CALL FAILED!")

    print("Error Type:")
    print(type(e).__name__)

    print("\nError:")
    print(e)