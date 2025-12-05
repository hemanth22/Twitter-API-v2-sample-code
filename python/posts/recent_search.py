"""
Recent Search - X API v2
========================
Endpoint: GET https://api.x.com/2/tweets/search/recent
Docs: https://developer.x.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN

Note: Returns posts from the last 7 days.
This example demonstrates automatic pagination using the iterate() method
to fetch all pages of results.
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

query = '(from:twitterdev -is:retweet) OR #twitterdev'

def main():
    # Search with automatic pagination
    all_posts = []
    for page in client.posts.search_recent(
        query=query,
        max_results=100,  # Per page
        tweetfields=["author_id"]
    ):
        all_posts.extend(page.data)
        print(f"Fetched {len(page.data)} Posts (total: {len(all_posts)})")
    
    print(f"\nTotal Posts: {len(all_posts)}")
    print(json.dumps({"data": all_posts[:5]}, indent=4, sort_keys=True))  # Print first 5 as example


if __name__ == "__main__":
    main()
