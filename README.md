<h1>:robot: Scraper w/ Discord Notification</h1>

A web scraper for Kijiji.ca based on your desired searches. You can also use excludes to prevent any unrelated items from triggering the notification script.
All notifications will be sent to your desired Discord channel via webhook.
*Tested on Ubuntu 18.04.03 LTS.*


<h2>Installation</h2>

Use git to pull the repository files to your machine in the /github/ directory:
>$ sudo git clone https://github.com/Fyre-Homelab/Scraper-Discord-Notification.git /github/

Install some required packages:
>$ sudo apt install python3-pip python3-bs4

Install some required packages for python:
>$ sudo pip3 install -r /github/Scraper-Discord-Notification/requirements.txt


<h2>Setup</h2>

Give main.py executable permissions.
>$ sudo chmod +x /github/Scraper-Discord-Notification/main.py

Open config.yaml to change some settings.
>$ sudo nano /github/Scraper-Discord-Notification/config.yaml


<h3>Get a Discord Webhook</h3>

Check out: https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks


<h3>config.yaml</h3>

**webhook:** insert the url provided by Discord. No quotations.

**bot name:** the name you want your webhook to use. No quotations.

**url's to scrape:** use a '-' followed by a space and the url of the kijiji search you want to be scraped. Repeat for each search.
```YAML
- url: https://www.kijiji.ca/b-free-stuff/manitoba/c17220001l9006
- url: https://www.kijiji.ca/b-cars-vehicles/manitoba/tesla/k0c27l9006
```

**terms to exclude from scraping:** include a list of terms that you want to exclude from being posted to Discord. Follows YAML spacing.
```YAML
- url: https://www.kijiji.ca/b-manitoba/lto/k0l9006
  exclude:
    - LTO1
    - LTO2
    - LTO3
    - LTO4
```


<h3>Initial Start-Up (Optional)</h3>

If it is your first time running the script, it may find ten to a few hundred search results, most of them will be older than you care to be bothered with.
So we can run the script manually once in "silent mode" by using the following command:

> sudo python3 /github/Scraper-Discord-Notification/main.py [-s]

This will populate a 'ads.json' file in the /github/Scraper-Discord-Notification/ file with all search results without sending you Discord notifications.
Then after you've set up a re-occurring check via crontab below, it will only search for new entries.


<h3>How to setup as a re-occurring check</h3>

>$ crontab -e
```bash
*/15 * * * * /github/Scraper-Discord-Notification/main.py
```
This sets it up to scrape every 15 minutes for example.

*NOTE: do not use 'sudo crontab -e' as it will not run properly!*


<h2>To-Do</h2>

- [x] How to get webhook
- [ ] Screenshots of notifications
- [x] Which files require editing (config.yaml)
- [x] How to setup searches/exclusions
- [x] Determine appropriate permissions for each file so that each file has the minimum appropriate permissions.
- [x] Remove dependance on hard-coded file locations so that it can be used by anyone in any desired directory.
- [ ] Investigate exclusions -- can we support RegEx? e.g. 2[0-9][8-9]0 to match with 2490, 2590, etc.