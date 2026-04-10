import discord

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
@listen
async def remove_listener():
    client.run("96ca5e09e390b8419105df6e27037a38202f6bcc1a76fdeeb8781488b92798e6")
    #class discord.ext.commands.Bot(command_prefix, *, help_command=<default-help-command>, tree_cls=<class 'discord.app_commands.tree.CommandTree'>, description=None, allowed_contexts=..., allowed_installs=..., intents, **options)
