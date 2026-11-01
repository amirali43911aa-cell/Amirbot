import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    markup.add(
        "👤 حساب کاربری",
        "💳 افزایش موجودی"
    )
    markup.add(
        "💎 خرید سرویس",
        "🎧 پشتیبانی"
    )

    bot.send_message(
        message.chat.id,
        "به ربات Amir v2 خوش اومدی 🌟\nیکی از گزینه‌ها رو انتخاب کن:",
        reply_markup=markup
    )

bot.infinity_polling()
