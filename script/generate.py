import json
import random
from datetime import datetime
import os

def generate_daily_challenge():
    # Load the pool of challenges
    pool_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'challenges_pool.json')
    
    with open(pool_path, 'r') as f:
        challenges = json.load(f)
        
    # Pick a random challenge
    challenge = random.choice(challenges)
    challenge["date"] = datetime.now().strftime("%Y-%m-%d")
    
    # Save to data/challenge.json
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'challenge.json')
    with open(output_path, 'w') as f:
        json.dump(challenge, f, indent=4)
    
    print(f"Daily challenge generated: {challenge['title']}")

if __name__ == "__main__":
    generate_daily_challenge()
