import logging
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from handler import start,ajuda
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    ajuda_handler = CommandHandler('ajuda', ajuda)
    application.add_handler(ajuda_handler)
    
    application.run_polling()


