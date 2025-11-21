#!/usr/bin/env python3
"""
Telegram Bot - Python File Encryptor
Military-Grade AES-256 Encryption
Powered by M0bsy
"""

import os
import sys
import tempfile
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from encryptor import PythonEncryptor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class EncryptorBot:
    def __init__(self, token):
        self.token = token
        self.encryptor = PythonEncryptor()
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = """
╔════════════════════════════════════════╗
║  🔐 PYTHON FILE ENCRYPTOR BOT 🔐       ║
║    Powered by M0bsy                    ║
║   Military-Grade AES-256 Security      ║
╚════════════════════════════════════════╝

Send me any Python file (.py) and I'll encrypt it with unbreakable military-grade encryption!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔐 AES-256 Military-Grade Encryption
  📦 Zlib Compression (Level 9)
  🔀 Triple Base64 Encoding
  ✓ SHA256 Integrity Verification
  🎲 20-Part Data Splitting
  📐 Anti-Decompiling Protection
  🛡️  Multi-Layer Obfuscation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 HOW TO USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  1️⃣  Send me a Python file (.py)
  2️⃣  I'll encrypt it instantly
  3️⃣  Download the encrypted file
  4️⃣  Run it like normal Python!

✅ The encrypted file works exactly like the original!
        """
        await update.message.reply_text(msg)
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = """
╔════════════════════════════════════════╗
║       📚 HOW TO USE THIS BOT 📚         ║
╚════════════════════════════════════════╝

1️⃣  Send me a Python file (.py extension)
2️⃣  Wait a few seconds while I encrypt it
3️⃣  Download the encrypted file I send back
4️⃣  Run it with: python encrypted_yourfile.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⌨️  COMMANDS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  /start  →  Start the bot
  /help   →  Show this help message
  /about  →  About this bot

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💬 Secure, unbreakable encryption!
        """
        await update.message.reply_text(msg)
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = """
╔════════════════════════════════════════╗
║         ℹ️  ABOUT THIS BOT ℹ️           ║
╚════════════════════════════════════════╝

📌 Python File Encryptor Bot
   Version: 3.0 (Military-Grade)
   Created by: M0bsy

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔐 MILITARY-GRADE ENCRYPTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ AES-256 Fernet Encryption
  ✓ Zlib Compression (Level 9)
  ✓ Triple Base64 Multi-Encoding
  ✓ SHA256 Integrity Checksum
  ✓ 20-Part Data Splitting
  ✓ Extreme Anti-Decompiling
  ✓ Impossible to decode!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files are IMPOSSIBLE to reverse engineer
while remaining fully functional!

🛡️  Protect your Python code!
        """
        await update.message.reply_text(msg)
    
    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        doc = update.message.document
        if not doc.file_name.endswith('.py'):
            await update.message.reply_text("❌ Please send a Python file (.py)!")
            return
        
        try:
            proc_msg = await update.message.reply_text("🔐 Encrypting with AES-256...\nPlease wait...")
            file = await doc.get_file()
            
            with tempfile.TemporaryDirectory() as temp_dir:
                in_path = os.path.join(temp_dir, doc.file_name)
                out_file = f"encrypted_{doc.file_name}"
                out_path = os.path.join(temp_dir, out_file)
                
                await file.download_to_drive(in_path)
                success = self.encryptor.encrypt_file(in_path, out_path)
                
                if not success:
                    await proc_msg.edit_text("❌ Encryption failed!")
                    return
                
                orig_sz = os.path.getsize(in_path)
                enc_sz = os.path.getsize(out_path)
                ratio = enc_sz / orig_sz
                
                caption = f"""╔════════════════════════════════════════╗
║   ✅ ENCRYPTION COMPLETE! ✅            ║
╚════════════════════════════════════════╝

📁 Original File:  {doc.file_name}
📁 Encrypted File: {out_file}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 STATISTICS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Original size:    {orig_sz:,} bytes
  Encrypted size:   {enc_sz:,} bytes
  Obfuscation ratio: {ratio:.2f}x

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔐 SECURITY APPLIED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ AES-256 Encryption
  ✓ Zlib Compression
  ✓ Triple Base64 Encoding
  ✓ SHA256 Checksum
  ✓ 20-Part Splitting
  ✓ Anti-Decompiling
  ✓ IMPOSSIBLE to decode!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
▶️  RUN WITH: python {out_file}

🔥 Powered by M0bsy
"""
                
                with open(out_path, 'rb') as f:
                    await update.message.reply_document(document=f, filename=out_file, caption=caption)
                
                await proc_msg.delete()
                logger.info(f"Encrypted {doc.file_name}")
                
        except Exception as e:
            logger.error(f"Error: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
    
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("📎 Send me a Python file (.py) to encrypt!\n\nUse /help for more info.")
    
    def run(self):
        app = Application.builder().token(self.token).build()
        app.add_handler(CommandHandler("start", self.start_command))
        app.add_handler(CommandHandler("help", self.help_command))
        app.add_handler(CommandHandler("about", self.about_command))
        app.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))
        
        print("╔═══════════════════════════════════════════════════════╗")
        print("║     Python Encryptor Bot - Running Successfully      ║")
        print("║              Powered by M0bsy                         ║")
        print("╚═══════════════════════════════════════════════════════╝")
        print("\n✅ Bot is online and ready!")
        print("📱 Send Python files to your bot")
        print("Press Ctrl+C to stop\n")
        
        app.run_polling(allowed_updates=Update.ALL_TYPES)

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        print("❌ ERROR: TELEGRAM_BOT_TOKEN not set!")
        print("\nSet it with: export TELEGRAM_BOT_TOKEN='your-token'")
        sys.exit(1)
    bot = EncryptorBot(token)
    bot.run()

if __name__ == "__main__":
    main()
