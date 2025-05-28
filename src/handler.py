from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Eu sou o secretario inteligente")


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("💡Irei te ajudar em breve!")