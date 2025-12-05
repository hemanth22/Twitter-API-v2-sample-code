"""
Full-Archive Tweet Counts - X API v2
====================================
Endpoint: GET https://api.x.com/2/tweets/counts/all
Docs: https://developer.x.com/en/docs/twitter-api/tweets/counts/api-reference/get-tweets-counts-all

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN

Note: Requires Academic Research access. Returns counts from the entire archive.
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

query = 'from:twitterdev'

def main():
    response = client.posts.get_tweet_counts_all(
        query=query,
        granularity="day",
        start_time="2021-01-01T00:00:00Z"
    )
    
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()