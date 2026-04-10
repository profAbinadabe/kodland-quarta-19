import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

lista_lixo = {
    "papel": "poucos meses. Não é dos mais poluentes",
    "plástico": "em torno de 300 a 400 anos. Um dos mais poluentes da atualidade",
    "metal": "em torno de 400 a 500 anos. Certos metais pesados podem prejudicar o solo",
    "vidro": "1000 anos ou mais",
    "lixo orgânico": "depende do tipo, mas geralmente entre alguns dias até dois meses"
}

lista_lixeiras_dicas = {
    "LIXEIRA AZUL": "papel",
    "LIXEIRA VERDE": "vidro",
    "LIXEIRA AMARELA": "metal",
    "LIXEIRA VERMELHA": "materiais tóxicos (baterias, instrumentos médicos etc)",
    "LIXEIRA MARROM": "materiais orgânicos"
}

@bot.event
async def on_ready():
    print(f'Logado como {bot.user} (ID: {bot.user.id})')
    print('O bot está pronto para te ajudar')

@bot.command()
async def help(ctx):
    mensagem = (
        "Este é o Bot Sustentável 🌱\n"
        "Use os seguintes comandos:\n"
        "$recycle <material>\n"
        "Exemplo: $recycle papel"
    )
    await ctx.send(mensagem)

@bot.command()
async def recycle(ctx, material: str):
    material = material.lower()

    if material in lista_lixo:
        await ctx.send(f"O tempo de decomposição do {material} é: {lista_lixo[material]}")
    else:
        await ctx.send("Material não encontrado. Tente: papel, plástico, metal, vidro ou lixo orgânico.")

bot.run("SEU_TOKEN_AQUI")
