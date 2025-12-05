"""
Reposted By (Users who reposted) - X API v2
============================================
Endpoint: GET https://api.x.com/2/tweets/:id/retweeted_by
Docs: https://developer.x.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweeted_by

Authentication: Bearer Token (App-only) or OAuth (User Context)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the post ID you want to get reposters for
post_id = "1354143047324299264"

def main():
    # Get reposted by users with automatic pagination
    all_users = []
    for page in client.posts.get_reposted_by(
        post_id,
        max_results=100,
        userfields=["created_at"]
    ):
        all_users.extend(page.data)
        print(f"Fetched {len(page.data)} users (total: {len(all_users)})")
    
    print(f"\nTotal Users: {len(all_users)}")
    print(json.dumps({"data": all_users[:5]}, indent=4, sort_keys=True))  # Print first 5 as example

if __name__ == "__main__":
    main()
