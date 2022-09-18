import feedparser
import markdownify
import requests
import json
import time

try:
    with open("config.json") as config:
        config = json.load(config)
except:
    raise FileNotFoundError("You have not created the config file under the name 'config.json'")

# first run, there is no 'cache' unless cache file is stored
if config['cache']:
    try:
        with open("cache.rss") as cache_file:
            cache = cache_file.read()
    except Exception as e:
        print("Error loading cache file.")
        cache = ""
else:
    cache = ""

# loop to check for new rss feed (essentially a listener)
while True:
    newsfeed = feedparser.parse(config['rss_feed_url']).entries
    if cache == str(newsfeed):
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
            "color": 0xad2f26
            }
        ],
        "username": config['discord_webhook_username'],
        "avatar_url": config['discord_webhook_avatar']
        })
        # set the 'cache' to the latest newsfeed obtained
        cache = newsfeed
        if config['cache']:
            with open('cache.rss', 'w+') as cache_file:
                cache_file.write(str(cache))
    time.sleep(config['check_interval']) # checks every x seconds (set in config)