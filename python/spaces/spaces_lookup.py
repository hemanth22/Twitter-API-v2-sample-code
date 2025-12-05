"""
Spaces Lookup - X API v2
========================
Endpoint: GET https://api.x.com/2/spaces
Docs: https://developer.x.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces

Authentication: Bearer Token (App-only) or OAuth (User Context)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Space IDs to look up (list)
space_ids = ["SPACE_ID"]

def main():
    # Optional params: host_ids, conversation_controls, created_at, creator_id, id, invited_user_ids,
    # is_ticketed, lang, media_key, participants, scheduled_start, speaker_ids, started_at, state, title, updated_at
    response = client.spaces.get_spaces(
        ids=space_ids,
        spacefields=["title", "created_at"],
        expansions=["creator_id"]
    )
    
    print(json.dumps(response.data, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()