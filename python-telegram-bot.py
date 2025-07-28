from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /payment, /refund, or /check_refund <order_id>.")

# /payment command
async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("To make a payment, visit: https://your-site.com/payment")

# /refund command
async def refund(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Refunds take 3-5 business days. Visit: https://your-site.com/refund")

# /check_refund command
async def check_refund(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        order_id = context.args[0]
        # Simulate refund status lookup
        await update.message.reply_text(f"Refund status for order {order_id}: In Progress")
    except IndexError:
        await update.message.reply_text("Usage: /check_refund <order_id>")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("payment", payment))
app.add_handler(CommandHandler("refund", refund))
app.add_handler(CommandHandler("check_refund", check_refund))

app.run_polling()
