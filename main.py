import sys
from core.matchmind_engine import MatchMindEngine

def main():
    print("=" * 70)
    print("                         MATCHMIND AI")
    print("              MULTI-AGENT CRICKET ANALYSIS")
    print("=" * 70)
    
    # Check for CLI arguments or ask interactively
    if len(sys.argv) > 1:
        match_id_str = sys.argv[1]
    else:
        match_id_str = input("\nEnter Cricbuzz Match ID (default: 40381): ").strip()
        
    if not match_id_str:
        match_id_str = "40381"
        
    try:
        match_id = int(match_id_str)
    except ValueError:
        print("\n[ERROR] Invalid Match ID. Please enter a valid number.")
        sys.exit(1)
        
    engine = MatchMindEngine()
    result = engine.process_match(match_id)
    
    if result.get("success"):
        print("\n" + "=" * 70)
        print("FINAL REPORT PREVIEW")
        print("=" * 70)
        print(result.get("final_report", "No report generated."))
    else:
        print("\n[ERROR] Engine failed to process the match.")

if __name__ == "__main__":
    main()