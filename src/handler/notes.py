from telegram  import Update
from telegram.ext import ContextTypes
from utils.Database import add_notes, list_notes, delete_note
from datetime import datetime

async def new_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    texto = ' '.join(context.args)
    if not texto:
        await update.message.reply_text(f"❗ Use /anotar <Sua anotação> ")
        return
    await update.message.reply_text(f"✅ Anotação salva, caso queira ver todas as suas anotações use /anotacoes \n Conteudo da sua anotação atual: \n 📝 {texto}")
    add_notes(user.id, texto)


async def list_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    notes = list_notes(user.id)
    if not notes:
        await update.message.reply_text("📭 Você ainda não tem nenhuma anotação.")
        return

    texto = "🗒️ *Suas anotações:*\n\n"
    for i, (_, note, created_at) in enumerate(notes, 1):
        dt = datetime.fromisoformat(created_at)
        data_formatada = dt.strftime("%d/%m/%Y às %H:%M")
        texto += f"{i}. {note} _(em {data_formatada})_\n"

    await update.message.reply_markdown(texto)

async def del_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("❗ Por favor, envie o número da anotação para deletar (exemplo: /delanotacoes 2)")
        return
    
    number = int(context.args[0])
    notes = list_notes(user.id)
    if number < 1 or number > len(notes):
        await update.message.reply_text(f"❗ Número inválido. Você tem {len(notes)} anotação(ões).")
        return

    note_id = notes[number - 1][0]
    print(note_id,user.id,number)
    delete_note(note_id,user.id)
    await update.message.reply_text(f"✅ Anotação número {number} deletada com sucesso!")


    

