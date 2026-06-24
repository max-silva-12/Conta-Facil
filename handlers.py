from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou o ContaFacil, seu assistente financeiro. Como posso ajudar?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # Por enquanto, mock do NLU
    resposta = f"Recebi: '{user_text}'. Em breve vou entender isso melhor!"

    await update.message.reply_text(resposta)