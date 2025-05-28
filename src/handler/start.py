from telegram  import Update
from telegram.ext import ContextTypes
from utils.Database import register_name, search_name



#Retorna a mensagem para o usuario após executar o comando.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = search_name(user.id)
    if name:
        return await update.message.reply_text(f"Seja bem vindo {user.first_name}")
    else:
        register_name(user.id, user.first_name)
        return await update.message.reply_text(f"Seja bem vindo {user.first_name}")
