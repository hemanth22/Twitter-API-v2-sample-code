"""
List Lookup by ID - X API v2
=============================
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

# You can replace the ID given with the List ID you wish to lookup.
list_id = "list-id"

def main():
    # List fields are adjustable, options include:
    # created_at, description, owner_id,
    # private, follower_count, member_count,
    response = client.lists.get_list(
        list_id,
        listfields=["created_at", "follower_count"]
    )
    
    print(json.dumps(response.data, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
