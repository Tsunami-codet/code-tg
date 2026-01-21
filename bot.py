from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8335010272:AAGvPyGLfPPdfZKmgzGuO_BNPflJRy9QeYs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Запустить гадание 🔮",
                web_app=WebAppInfo(
                    url="https://YOUR_WEBAPP_URL"  # заменим на реальный URL
                ),
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Открой приложение для гадания на Таро:", reply_markup=reply_markup
    )

if __name__ == "__main__":
    print("Бот стартует...")
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("Бот работает...")
    app.run_polling()
