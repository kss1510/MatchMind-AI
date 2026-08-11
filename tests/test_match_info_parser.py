from api.cricbuzz_client import CricbuzzClient
from api.cricbuzz_parser import parse_match_info


def main():

    print("=" * 60)
    print("CRICBUZZ MATCH INFO PARSER TEST")
    print("=" * 60)

    client = CricbuzzClient()

    try:

        raw_data = client.get_match_info(40381)

        print("\nAPI call successful!")

        match_info = parse_match_info(raw_data)

        print("\nParsed Match Info:")
        print(match_info)

        print("\n" + "=" * 60)
        print("MATCH INFO PARSER TEST SUCCESSFUL!")
        print("=" * 60)

    except Exception as e:

        print("\nMATCH INFO PARSER TEST FAILED!")
        print("Error Type:")
        print(type(e).__name__)

        print("\nError:")
        print(e)


if __name__ == "__main__":
    main()