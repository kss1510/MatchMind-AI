from core.matchmind_engine import MatchMindEngine

MATCH_ID = 40381

print("=" * 60)
print("MATCHMIND AI - STEP 4 ENGINE TEST")
print("=" * 60)

try:
    print("\nRunning MatchMind Engine (Lightweight Validation Mode)...")

    engine = MatchMindEngine()
    result = engine.process_match(MATCH_ID, execute_pipeline=False)

    if not result.get("success"):
        raise Exception(result.get("error"))

    print("\n" + "=" * 60)
    print("LIGHTWEIGHT VALIDATION RESULTS")
    print("=" * 60)
    print(result.get("message"))
    
    match_context = result.get("match_context")
    if match_context:
        print("\nMatch Context initialized successfully!")
        print(f"Team: {match_context.team}")
        print(f"Opponent: {match_context.opponent}")
        print(f"Venue: {match_context.venue}")
        print(f"Format: {match_context.format}")
        print(f"Date: {match_context.match_date}")
        
    print("\n" + "=" * 60)
    print("MATCHMIND AI STEP 4 ENGINE TEST SUCCESSFUL!")
    print("=" * 60)

except Exception as e:
    print("\n" + "=" * 60)
    print("STEP 4 ENGINE TEST FAILED!")
    print("=" * 60)
    print(f"\nError Type: {type(e).__name__}")
    print(f"\nError: {e}")
    raise