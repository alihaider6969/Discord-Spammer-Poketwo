from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    "985112580265738300":
    "Nzc1MjQ0NjMxMzIzNTc0Mjky.GSyK-L.shsfzkLU3di9bUEkebrEJ6xUglZel71A_FJrm8"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
