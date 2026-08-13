import os
import requests

USER_ID = 2334071257
WEBHOOK = os.environ["DISCORD_WEBHOOK"]

response = requests.post(
    "https://presence.roblox.com/v1/presence/users",
    json={"userIds": [USER_ID]}
)

data = response.json()["userPresences"][0]
status = data["userPresenceType"]

previous_file = "previous_status.txt"

try:
    with open(previous_file, "r") as f:
        previous = int(f.read())
except FileNotFoundError:
    previous = 0

if status == 2 and previous != 2:
    requests.post(WEBHOOK, json={
        "content": "🔔 **emilydance62 is now online on Roblox!**"
    })

with open(previous_file, "w") as f:
    f.write(str(status))
