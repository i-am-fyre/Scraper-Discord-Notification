#!/usr/bin/env python3

import yaml
import sys

from kijiji_scraper.kijiji_scraper import KijijiScraper
from kijiji_scraper.discord_client import DiscordClient

if __name__ == "__main__":
    args = sys.argv
    skip_flag = "-s" in args

    # Get config values
    with open("/home/scraper/Kijiji-Scraper-Discord/config.yaml", "r") as config_file:  ## This is specific to my machine, will "./config.yaml" work?
        discord_config, urls_to_scrape = yaml.safe_load_all(config_file)

    # Initialize the KijijiScraper
    kijiji_scraper = KijijiScraper()
    discord_client = DiscordClient(discord_config)

    # Scrape each url given in config file
    for url_dict in urls_to_scrape:
        url = url_dict.get("url")
        exclude_words = url_dict.get("exclude", [])

        print(f"Scraping: {url}")
        if len(exclude_words):
            print("Excluding: " + ", ".join(exclude_words))

        kijiji_scraper.set_exclude_list(exclude_words)
        ads, discord_title = kijiji_scraper.scrape_kijiji_for_ads(url)

        info_string = f"Found {len(ads)} new ads\n" \
            if len(ads) != 1 else "Found 1 new ad\n"
        print(info_string)

        if not skip_flag and len(ads):
            discord_client.send_ads(ads, discord_title)

    kijiji_scraper.save_ads()