import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CANAL_OBJETIVO = int(os.getenv("CHANNEL_ID", "0"))  # ID del canal donde querés que responda

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    print(f"📢 Monitoreando el canal con ID: {CANAL_OBJETIVO}")

@bot.event
async def on_message(message):
    # Ignorar mensajes de TODOS los bots para evitar bucles infinitos
    if message.author.bot:
        return

    # Canal específico donde debe responder
    if message.channel.id == CANAL_OBJETIVO:
        # Acá podés decidir qué responder según el mensaje
        contenido = message.content.lower()

        # Detectar cualquier mención de UHC
        if "uhc" in contenido:
            await message.channel.send("<@&1434286826771709992> ALERTA DE UHC")

    # Importante para que los comandos sigan funcionando
    await bot.process_commands(message)

if __name__ == "__main__":
    if not TOKEN:
        print("❌ Error: DISCORD_BOT_TOKEN no está configurado en las variables de entorno.")
        print("Por favor, agregá tu token de Discord en los Secrets de Replit.")
        exit(1)
    
    if CANAL_OBJETIVO == 0:
        print("⚠️ Advertencia: CHANNEL_ID no está configurado. El bot no responderá a ningún canal.")
        print("Por favor, configurá CHANNEL_ID con el ID del canal que querés monitorear.")
    
    bot.run(TOKEN)