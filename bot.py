from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8790130366:AAERmnKuOQS1UNUOeS6lEULU3tNyLrwLWWs"

LINK1 = "https://mpago.la/2qbTxZn"
LINK2 = "https://mpago.la/2SsVm9T"
LINK3 = "https://mpago.la/1QfyvhX"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        [InlineKeyboardButton("💖 Pack 1 - R$19,90", url=LINK1)],
        [InlineKeyboardButton("💖 Pack 2 - R$29,90", url=LINK2)],
        [InlineKeyboardButton("💖 Pack 3 - R$39,90", url=LINK3)],
    ]

    texto = """
Oii, meu nome é Rafaella e estou vendendo fotos pra pagar minha faculdade ❤️

Tenho 3 opções disponíveis:

💖 Pack 1 - R$19,90
💖 Pack 2 - R$29,90
💖 Pack 3 - R$39,90

Escolha uma opção abaixo:
"""

    await update.message.reply_text(
        texto,
        reply_markup=InlineKeyboardMarkup(teclado)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()