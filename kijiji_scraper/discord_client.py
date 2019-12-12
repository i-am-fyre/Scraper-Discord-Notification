#!/bin/usr/env python3
import discord
import subprocess
import os
from pathlib import Path


class DiscordClient():

    def __init__(self, discord_config):
        self.webhook_url = discord.Webhook.from_url(discord_config.get("WebhookURL"), adapter=discord.RequestsWebhookAdapter())
        self.webhook_name = discord_config.get("WebhookName")
        self.update_notification = discord_config.get("UpdateNotification")
        self.update_count = discord_config.get("UpdateCount")

        self.current_directory = os.path.dirname(os.path.realpath(__file__))
        filename = self.current_directory + "/../variables/update_notification_count.txt"
        self.filepath = Path().absolute().joinpath(filename)

        f = open(self.filepath,"r")
        update_notification_count = int(f.read())

        if self.update_notification and (update_notification_count >= self.update_count):
            self.check_version(update_notification_count)
        else:
            update_notification_count = update_notification_count + 1

            file = open(self.filepath,"w+")
            file.write(str(update_notification_count))
            file.close()

        f = open(self.filepath,"r")
        update_notification_count = int(f.read())

    # Sends a Discord message with links and info of new ads
    def send_ads(self, ad_dict, discord_title):
        title = self.__create_discord_title(discord_title, len(ad_dict))

        result = self.webhook_url.send(content=f"**{title}**", username=self.webhook_name)

        for ad_id in ad_dict:
            embed = self.__create_discord_embed(ad_dict, ad_id)

            self.webhook_url.send(embed=embed, username=self.webhook_name)

    def __create_discord_title(self, discord_title, ad_count):
        if ad_count > 1:
            return str(ad_count) + ' New ' + discord_title + ' Ads Found!'

        return 'One New ' + discord_title + ' Ad Found!'

    def __create_discord_embed(self, ad_dict, ad_id):

        embed = discord.Embed()
        embed.colour = discord.Colour.green()
        embed.url=ad_dict[ad_id]['Url']

        try:
            embed.title = f"{ad_dict[ad_id]['Title']}"

            if ad_dict[ad_id]['Location'] != "":
                embed.add_field(name="Location", value=ad_dict[ad_id]['Location'])

            if ad_dict[ad_id]['Date'] != "":
                embed.add_field(name="Date", value=ad_dict[ad_id]['Date'])

            if ad_dict[ad_id]['Price'] != "":
                embed.add_field(name="Price", value=ad_dict[ad_id]['Price'])

            if ad_dict[ad_id]['Description'] != "":
                embed.add_field(name="Description", value=ad_dict[ad_id]['Description'], inline=False)

            if ad_dict[ad_id]['Details'] != "":
                embed.add_field(name="Details", value=ad_dict[ad_id]['Details'], inline=False)

        except KeyError:
            embed.title = f"{ad_dict[ad_id]['Title']}"

        return embed

    def check_version(self, update_notification_count):

        GIT_DIR = self.current_directory + '/../.git/'

        LOCAL=subprocess.check_output(['git', 'rev-parse', '@'], env={'GIT_DIR': GIT_DIR}, stdin=None, stderr=None, shell=False, universal_newlines=False)
        REMOTE=subprocess.check_output(['git', 'rev-parse', '@{u}'], env={'GIT_DIR': GIT_DIR}, stdin=None, stderr=None, shell=False, universal_newlines=False)

        if (LOCAL != REMOTE) :
            #Send Discord Notification.
            embed = discord.Embed()
            embed.colour = discord.Colour.purple()
            embed.url = "https://github.com/Fyre-Homelab/Fyre-Scraper-Dev"
            embed.title = f"New Update Available"
            self.webhook_url.send(embed=embed, username=self.webhook_name)

            update_notification_count = 0

            file = open(self.filepath,"w+")
            file.write(str(update_notification_count))
            file.close()