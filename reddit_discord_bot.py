import praw
import requests

# Reddit API credentials - replace with your own values
reddit = praw.Reddit(client_id='pT0ffVcgq33VNsIxJNrSJQ',
                     client_secret='ukF7pMQnDgy-TGyz6ll2IQAcDfXiSQ',
                     username='Effective_Ear_425',
                     password='Krish@1502',
                     user_agent='MyRedditBot/0.1 by u/Effective_Ear_425')

# Connect to the subreddit you want to monitor
subreddit = reddit.subreddit('target_subreddit')  # Replace 'target_subreddit' with desired subreddit name

# Discord webhook URL
discord_webhook_url = 'https://discord.com/api/webhooks/1436644163759243405/pkjVtAEEkvCTg6LJH3nD12THUi-v2QPmdLDzVahoHst4NYd6eQxYV02XNNjxR7yIPEcO'

# Function to send message to Discord channel
def send_to_discord(message):
    data = {"content": message}
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send message: {response.text}")

# Send a test message to Discord
send_to_discord("Hello from Reddit bot!")

print("Bot is set up and ready.")
# Stream new submissions from the subreddit
for submission in subreddit.stream.submissions(skip_existing=True):
    message = f"New post in r/{subreddit.display_name}:\n**{submission.title}**\n{submission.url}"
    send_to_discord(message)
    print(f"Sent to Discord: {submission.title}")
