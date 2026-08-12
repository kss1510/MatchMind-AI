
# Simplify all specialist agent prompts to 3 sections for faster LLM inference

import re

AGENTS = {
    'agents/team_selection/team_agent.py': (
        # match task description block
        r'(task = Task\(\s*\n\s*description=f""")(.*?)(""",\s*\n\s*expected_output=""")(.*?)(""",\s*\n\s*agent=agent)',
        lambda m: (
            m.group(1) +
            '\n{ctx}\n\nBased ONLY on the scorecard above, give a brief team selection report.\n'
            '1. Top performers to retain (from batting/bowling stats)\n'
            '2. Players to reconsider (worst performers)\n'
            '3. Key selection recommendation\n\nUse only facts from the data. If data is missing, say so.\n' +
            m.group(3) +
            '\nA concise team selection report with 3 sections:\n'
            '1. Performers to Retain\n2. Players to Reconsider\n3. Key Recommendation\n' +
            m.group(5)
        )
    ),
    'agents/performance/performance_agent.py': (
        r'(task = Task\(\s*\n\s*description=f""")(.*?)(""",\s*\n\s*expected_output=""")(.*?)(""",\s*\n\s*agent=agent)',
        lambda m: (
            m.group(1) +
            '\n{ctx}\n\nBased ONLY on the scorecard above, give a brief performance report.\n'
            '1. Best batting performance (top scorer: name, runs, strike rate)\n'
            '2. Best bowling performance (top bowler: name, wickets, economy)\n'
            '3. Overall match assessment in 1-2 sentences\n\nUse only statistics shown. If data missing, say so.\n' +
            m.group(3) +
            '\nA concise performance report with 3 sections:\n'
            '1. Best Batting Performance\n2. Best Bowling Performance\n3. Overall Assessment\n' +
            m.group(5)
        )
    ),
    'agents/fitness/fitness_agent.py': (
        r'(task = Task\(\s*\n\s*description=f""")(.*?)(""",\s*\n\s*expected_output=""")(.*?)(""",\s*\n\s*agent=agent)',
        lambda m: (
            m.group(1) +
            '\n{ctx}\n\nBased ONLY on the scorecard above, give a brief fitness report.\n'
            '1. Players with high workload (many overs bowled or long batting innings)\n'
            '2. Players who may need rest (low contribution)\n'
            '3. Fitness recommendation for the next match\n\nUse only statistics shown. If data missing, say so.\n' +
            m.group(3) +
            '\nA concise fitness report with 3 sections:\n'
            '1. High Workload Players\n2. Rest Candidates\n3. Fitness Recommendation\n' +
            m.group(5)
        )
    ),
    'agents/opponent/opponent_agent.py': (
        r'(task = Task\(\s*\n\s*description=f""")(.*?)(""",\s*\n\s*expected_output=""")(.*?)(""",\s*\n\s*agent=agent)',
        lambda m: (
            m.group(1) +
            '\n{ctx}\n\nBased ONLY on the scorecard above, give a brief opponent analysis.\n'
            '1. Opponent key batsmen (highest scorers with strike rates)\n'
            '2. Opponent key bowlers (most wickets, best economy)\n'
            '3. Main tactical threat to address\n\nUse only statistics shown. If data missing, say so.\n' +
            m.group(3) +
            '\nA concise opponent analysis with 3 sections:\n'
            '1. Key Batsmen\n2. Key Bowlers\n3. Main Tactical Threat\n' +
            m.group(5)
        )
    ),
}

for path, (pattern, replacer) in AGENTS.items():
    txt = open(path, encoding='utf-8').read()
    # Find the task description block using dotall
    m = re.search(pattern, txt, re.DOTALL)
    if m:
        # Build new description — inject {match_context.to_prompt()} placeholder
        new_block = replacer(m)
        new_block = new_block.replace('{ctx}', '{match_context.to_prompt()}')
        new_txt = txt[:m.start()] + new_block + txt[m.end():]
        open(path, 'w', encoding='utf-8').write(new_txt)
        print(f'Updated: {path}')
    else:
        print(f'NO MATCH for pattern in: {path}')

print('All done.')
