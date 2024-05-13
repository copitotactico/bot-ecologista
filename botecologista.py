import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    if message.content.startswith('$planeta'):
        await message.channel.send("cuidalo por que es lo mas importante")
    if message.content.startswith("$GG"):
        await message.channel.send("GG bro")
    if message.content.startswith("$naturaleza"):
        await message.channel.send("CUIDA A TU PLANETA")
    if message.content.startswith("$Warzone"):
        await message.channel.send("let's Play bro")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)
    
