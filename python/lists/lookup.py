"""
List Lookup - X API v2
======================
Endpoint: GET https://api.x.com/2/lists/:id
Docs: https://developer.x.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-lists-id

Authentication: Bearer Token (App-only) or OAuth (User Context)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the list ID you want to look up
list_id = "84839422"

def main():
    # List fields are adjustable. Options include:
    # created_at, follower_count, member_count, private, description, owner_id
    response = client.lists.get_list(
        list_id,
        listfields=["created_at", "follower_count", "member_count", "owner_id", "description"]
    )
    
    print(json.dumps(response.data, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
