import os

import discord
from dotenv import load_dotenv
import csv
import pandas as pd

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


def find_totals(username):
    totals = open("totals.csv")
    dt = csv.DictReader(totals)
    if dt


    # with open("F:/Documents/CS141/DiscordBot/totals.csv", "w+") as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     add_new = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     for row in csv_reader:
    #         if row[0] == username:
    #             add_new.writerow([username, int(row[1]) + 10, int(row[2]) + 10])
    #             return row[1], row[2]
    #     add_new.writerow([username, "10", "10"])
    #     return 10, 10


def reset_daily():
    df = pd.read_csv("totals.csv")
    df["dailyTotal"] = df["dailyTotal"].replace("0")
    df.to_csv("dailyTotal.csv", index=False)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!error":
        total, daily = find_totals(message.author)
        response = f"Do ten! \n All Time Total: {total} Daily Total: {daily}"
        await message.channel.send(response)

client.run(TOKEN)
