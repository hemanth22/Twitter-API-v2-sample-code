"""
User Posts Timeline - X API v2
==============================
Endpoint: GET https://api.x.com/2/users/:id/tweets
Docs: https://developer.x.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-tweets

Authentication: Bearer Token (App-only) or OAuth (User Context)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the user ID you want to get posts for
user_id = "2244994945"

def main():
    # Get user posts with automatic pagination
    # Post fields are adjustable. Options include:
    # attachments, author_id, context_annotations, conversation_id,
    # created_at, entities, geo, id, in_reply_to_user_id, lang,
    # possibly_sensitive, public_metrics, referenced_tweets, source, text
    all_posts = []
    for page in client.users.get_tweets(
        user_id,
        max_results=100,
        tweetfields=["created_at"]
    ):
        all_posts.extend(page.data)
        print(f"Fetched {len(page.data)} posts (total: {len(all_posts)})")
    
    print(f"\nTotal Posts: {len(all_posts)}")
    print(json.dumps({"data": all_posts[:5]}, indent=4, sort_keys=True))  # Print first 5 as example

if __name__ == "__main__":
    main()
