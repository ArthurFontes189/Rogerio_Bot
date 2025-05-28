import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler,CallbackQueryHandler
from handler.start import start
from handler.notes import new_note, list_note,del_note

#Bot TOKEN
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")



#Log do bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Identifica quando o usuario executa um comando.
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    note_handler = CommandHandler('anotar', new_note)
    application.add_handler(note_handler)

    Searchnote_handler = CommandHandler('anotacoes', list_note)
    application.add_handler(Searchnote_handler)

    delnote_handler = CommandHandler('delanotacoes', del_note)
    application.add_handler(delnote_handler)

    application.run_polling()


