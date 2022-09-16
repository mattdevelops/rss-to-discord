## RSS Feed to Discord webhook

Python program that looks up and refreshes a RSS feed every *x* amount of seconds where *x* defined by user.
The program then posts the RSS feed to a Discord webhook if there has been a new RSS feed found.
Recommended to be run on a ([Ubuntu](https://ubuntu.com/download/server)) server using a process manager ([PM2](https://www.npmjs.com/package/pm2) recommended). You could also use a cloud platform service (PaaS) to run the code such as [Heroku](https://www.heroku.com/).

### Setup (using a server)
1. Ensure you have [Python 3](https://www.python.org/downloads/) installed on your server of choice
2. Install the requirements for this package using `pip install -r requirements.txt`
3. Copy `default-config.json` to `config.json` and add the appropriate blank values
4. Using your process manager, setup main.py to run. I recommend using PM2 so it would be `pm2 start rss-to-discord --interpreter python3 main.py` 
5. Complete! Every time the RSS feed updates, the latest post will be sent to the Discord webhook

### Example usage
I use this program to send the latest SCS Software updates to the [Prime Logistics](https://discord.gg/prime) Discord guild.