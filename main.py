import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# إعدادات التوكن
TOKEN = "7914085819:AAEGLKRDMQn5P7RPPc41khdHT2LBp7yMjOk"

# إعداد السجلات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# قائمة الأسماء المسموح لها باستخدام البوت
allowed_users = {
    "يوسف كراسي", "عبد الناصر شوا", "محمود حميد", "محمد سيف الحسين", "محمد طراب",
    "غيث الحسيني", "محمود عويجة", "احمد بارودجي", "احمد مغربي", "عدنان سجادة",
    "وسيم نجار", "يوسف كزارة", "عبد الله عبدان", "محمد زين دباس", "جمال لجنوني",
    "جمال الدور", "عبد العزيز جعارة", "احمد منال اسامة الزهراني", "محمد خصيم",
    "فاروق قلة", "بلال الحسن", "عمر دياب خضورة", "قتيبة قصلب", "زيد حمامي", "احمد منال"
}

# دالة بدء البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    full_name = f"{update.effective_user.first_name} {update.effective_user.last_name or ''}".strip()
    if full_name not in allowed_users:
        await update.message.reply_text("❌ اسمك غير مسموح له باستخدام هذا البوت.")
        return
    await update.message.reply_text(f"أهلاً {full_name}! اختر المادة يلي بدك إياها:")

# دالة استقبال الرسائل
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم استلام رسالتك.")

# البرنامج الرئيسي
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("البوت يعمل حالياً...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())