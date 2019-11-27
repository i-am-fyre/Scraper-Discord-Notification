<h1>:robot: Scraper Discord Notification</h1>
A web scraper for Kijiji.ca based on your desired searches. You can also use excludes to prevent any unrelated items from triggering the notification script.
All notifications will be sent to your desired Discord channel via webhook.


<h2>Setup</h2>
Copy all files to your computer/server. Give appropriate permissions to the files so that they can be executed.


**How to setup as a re-occurring check**
>$ sudo crontab -e
```bash
*/7 * * * * python3 /home/scraper/Kijiji-Scraper-Discord/main.py  #replace with the proper location of your main.py file
```
This sets it up to scrape every 7 minutes for example.

*Note: The information above is not complete. When I tinker, I will update the information, or you can submit a pull request with more information.*


<h2>To-Do</h2>
- [ ] How to get webhook
- [ ] Screenshots of notifications
- [ ] Which files require editing (config.yaml)
- [ ] How to setup searches/exclusions
- [ ] Determine appropriate permissions for each file so that each file has the minimum appropriate permissions.
- [ ] Remove dependance on hard-coded file locations so that it can be used by anyone in any desired directory.