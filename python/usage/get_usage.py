"""
Usage Posts - X API v2
======================
Endpoint: GET https://api.x.com/2/usage/tweets
Docs: https://developer.x.com/en/docs/twitter-api/usage/api-reference/get-usage-tweets

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN

Returns the number of posts read from the API.
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

def main():
    response = client.usage.get_tweets_usage(days=7)
    
    print(json.dumps(response.data, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
