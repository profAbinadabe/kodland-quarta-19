import discord
import os
import random
from discord.ext import commands
import requests




intents = discord.intents.default()
intents.message_content = True
bot = discord.Bot(command_prefix="$", intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']




@bot.command('meme')
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))

    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.file(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("SEU TOKEN AQUI")