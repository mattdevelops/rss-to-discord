import feedparser
import markdownify
import requests
import json
import time

with open("config.json") as config:
    config = json.load(config)

# first run, there is no 'cache'
cache = ""

while True:
    newsfeed = feedparser.parse(config['rss_feed_url']).entries
    if cache == newsfeed:
        pass # there has been no update to the RSS feed compared to the cache so nothing will be done
    else:
        # get first section of summary for embed
        summary = newsfeed[0]['summary']
        summary = markdownify.markdownify(summary, heading_style="ATX").splitlines()
        output = ""
        for line in summary:
            if line == "":
                break
            output += line

        # get title and link to blog post
        title = newsfeed[0]['title']
        link = newsfeed[0]['link']

        # post the embed to discord webhook
        request = requests.post(config['discord_webhook_url'], json={
        "content": link,
        "embeds": [
            {
            "title": f":newspaper: | {title}",
            "description": output,
            "url": link,
            "color": 5814783
            }
        ],
        "username": config['discord_webhook_username'],
        "avatar_url": config['discord_webhook_avatar']
        })
        # set the 'cache' to the latest newsfeed obtained
        cache = newsfeed
    time.sleep(config['check_interval']) # checks every x seconds (set in config)