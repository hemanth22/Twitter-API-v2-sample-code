"""
Recent Tweet Counts - X API v2
==============================
Endpoint: GET https://api.x.com/2/tweets/counts/recent
Docs: https://developer.x.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-recent

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN

Note: Returns count of posts from the last 7 days matching your query.
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

query = 'from:twitterdev'

def main():
    response = client.posts.get_tweet_counts_recent(
        query=query,
        granularity="day"
    )
    
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
