import os
import asyncio
from aiogram import Bot

# ===============================
# CONFIGURAÇÕES
# ===============================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = -1001234567890  # substitua pelo ID real do seu canal

# ===============================
# FUNÇÃO DE TESTE
# ===============================
async def enviar_mensagem_teste():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(CHAT_ID, "✅ BOT INICIALIZOU E CONSEGUE ENVIAR MENSAGEM!")
    await bot.session.close()  # fecha sessão corretamente

# ===============================
# INICIALIZAÇÃO
# ===============================
if __name__ == "__main__":
    print("DEBUG: Iniciando bot de teste...")
    asyncio.run(enviar_mensagem_teste())
