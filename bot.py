from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 🎴 Я Таро‑бот с гаданиями и гороскопом.\n"
        "Открой Web App: https://YOUR_VERCEL_URL.vercel.app/"
    )

async def horoscope(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Выберите свой знак зодиака на сайте, чтобы получить персональный гороскоп! 🌟"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("horoscope", horoscope))

print("Бот запускается... 🚀")
app.run_polling()
