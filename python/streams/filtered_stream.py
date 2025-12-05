"""
Filtered Stream - X API v2
==========================
Endpoint: GET https://api.x.com/2/tweets/search/stream
Docs: https://developer.x.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/get-tweets-search-stream

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN

Note: Streams posts matching your filter rules in real-time.
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

def get_rules():
    response = client.streams.get_rules()
    print(json.dumps(response.data, indent=4, sort_keys=True))
    return response.data


def delete_all_rules(rules):
    if rules is None or not rules:
        return None

    ids = [rule["id"] for rule in rules]
    payload = {"delete": {"ids": ids}}
    response = client.streams.delete_rules(body=payload)
    print(json.dumps(response.data, indent=4, sort_keys=True))


def set_rules():
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "dog has:images", "tag": "dog pictures"},
        {"value": "cat has:images -grumpy", "tag": "cat pictures"},
    ]
    payload = {"add": sample_rules}
    response = client.streams.add_rules(body=payload)
    print(json.dumps(response.data, indent=4, sort_keys=True))


def get_stream():
    # Stream posts matching the filter rules in real-time
    for post in client.streams.get_filtered_stream():
        print(json.dumps(post.data, indent=4, sort_keys=True))


def main():
    rules = get_rules()
    delete_all_rules(rules)
    set_rules()
    get_stream()


if __name__ == "__main__":
    main()
