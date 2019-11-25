#!/bin/usr/env python3
import requests
import json

class DiscordClient():

    def __init__(self, discord_config):
        self.webhook = discord_config.get("webhook")
        self.bot_name = discord_config.get("bot name")

    # Sends a Discord message with links and info of new ads
    def send_ads(self, ad_dict, discord_title):
        title = self.__create_discord_title(discord_title, len(ad_dict))
        data = {}
        data["content"] = "[" + title + "]"
        data["username"] = self.bot_name

        result = requests.post(self.webhook,data=json.dumps(data), headers={"Content-Type": "application/json"})

        for ad_id in ad_dict:
            message = self.__create_discord_message(ad_dict, ad_id)

            data = {}
            data["content"] = message
            data["username"] = self.bot_name

            result = requests.post(self.webhook,data=json.dumps(data), headers={"Content-Type": "application/json"})

    def __create_discord_title(self, discord_title, ad_count):
        if ad_count > 1:
            return str(ad_count) + ' New ' + discord_title + ' Ads Found!'

        return 'One New ' + discord_title + ' Ad Found!'

    def __create_discord_message(self, ad_dict, ad_id):
        body = ''
        try:
            body += '```\n'

            body += '[ ' + ad_dict[ad_id]['Location'] + ' ] '

            body += ad_dict[ad_id]['Title'] + ' '

            if ad_dict[ad_id]['Date'] != "":
                body += ' - Posted on: ' +  ad_dict[ad_id]['Date'] + ' - '

            body += ad_dict[ad_id]['Description'] + ' '

            if ad_dict[ad_id]['Details'] != '':
                body += ad_dict[ad_id]['Details'] + ' '

            body += '[ ' + ad_dict[ad_id]['Price'] + ' ]\n```'

            body += ad_dict[ad_id]['Url'] + '\n'

        except KeyError:
            body += ad_dict[ad_id]['Title'] + ' '
            body += ad_dict[ad_id]['Url'] + ' '

        return body