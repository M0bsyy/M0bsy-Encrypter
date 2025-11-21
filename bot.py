#!/usr/bin/env python3
"""
Telegram Bot - Python File Encryptor
Automatically encrypts Python files sent to the bot
Powered by M0bsy
"""

import os
import sys
import tempfile
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Import the encryptor
from encryptor import PythonEncryptor

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class EncryptorBot:
    def __init__(self, token):
        self.token = token
        self.encryptor = PythonEncryptor()
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send welcome message when /start is used"""
        welcome_message = """
🔐 *Python File Encryptor Bot*
_Powered by M0bsy_

Send me any Python file (.py) and I'll encrypt it with 5 layers of advanced obfuscation!

*Features:*
• XOR Encryption with random keys
• Marshal bytecode compilation
• Zlib compression
• Base64 + Base85 + Hex encoding
• Random variable names
• Junk code injection
• 7-8x file size increase

*How to use:*
1. Send me a Python file (.py)
2. I'll encrypt it instantly
3. Download the encrypted file
4. Run it like normal Python!

_The encrypted file works exactly like the original!_
        """
        await update.message.reply_text(welcome_message, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send help message when /help is used"""
        help_message = """
📚 *How to Use This Bot*

1️⃣ Send me a Python file (.py extension)
2️⃣ Wait a few seconds while I encrypt it
3️⃣ Download the encrypted file I send back
4️⃣ Run it with: `python encrypted_yourfile.py`

*Commands:*
/start - Start the bot
/help - Show this help message
/about - About this bot

*Note:* The encrypted file is 7-8x larger but works identically to the original!
        """
        await update.message.reply_text(help_message, parse_mode='Markdown')
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send about message when /about is used"""
        about_message = """
ℹ️ *About This Bot*

*Python File Encryptor Bot*
Version: 1.0
Created by: M0bsy

This bot uses advanced 5-layer obfuscation:
• XOR encryption with 32-char random keys
• Marshal bytecode compilation
• Zlib compression (level 9)
• Base64, Base85, and Hex encoding
• Random variable name obfuscation
• Junk code injection
• Split data execution

The encrypted files are extremely difficult to reverse engineer while remaining fully functional.

_Protect your Python code from casual copying!_
        """
        await update.message.reply_text(about_message, parse_mode='Markdown')
    
    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming documents (Python files)"""
        document = update.message.document
        
        # Check if it's a Python file
        if not document.file_name.endswith('.py'):
            await update.message.reply_text(
                "❌ Please send a Python file (.py extension only)!"
            )
            return
        
        try:
            # Send processing message
            processing_msg = await update.message.reply_text(
                "🔐 Encrypting your Python file...\nPlease wait..."
            )
            
            # Download the file
            file = await document.get_file()
            
            # Create temporary directory for processing
            with tempfile.TemporaryDirectory() as temp_dir:
                input_path = os.path.join(temp_dir, document.file_name)
                output_filename = f"encrypted_{document.file_name}"
                output_path = os.path.join(temp_dir, output_filename)
                
                # Download file to temp directory
                await file.download_to_drive(input_path)
                
                # Encrypt the file
                success = self.encryptor.encrypt_file(input_path, output_path)
                
                if not success:
                    await processing_msg.edit_text(
                        "❌ Encryption failed! Make sure the file is valid Python code."
                    )
                    return
                
                # Get file sizes
                original_size = os.path.getsize(input_path)
                encrypted_size = os.path.getsize(output_path)
                ratio = encrypted_size / original_size
                
                # Send the encrypted file back
                caption = f"""✅ *Encryption Complete!*

📁 Original: `{document.file_name}`
📁 Encrypted: `{output_filename}`

📊 *Stats:*
• Original size: {original_size:,} bytes
• Encrypted size: {encrypted_size:,} bytes
• Obfuscation ratio: {ratio:.2f}x

🔐 *Security:*
• 5 layers of encryption applied
• XOR + Marshal + Zlib + Base64 + Base85 + Hex
• Random variable names
• Junk code injection
• Extremely difficult to reverse engineer

_Run with: python {output_filename}_

🔥 Powered by M0bsy
"""
                
                # Send the encrypted file
                with open(output_path, 'rb') as encrypted_file:
                    await update.message.reply_document(
                        document=encrypted_file,
                        filename=output_filename,
                        caption=caption,
                        parse_mode='Markdown'
                    )
                
                # Delete processing message
                await processing_msg.delete()
                
                logger.info(f"Successfully encrypted {document.file_name} for user {update.effective_user.id}")
                
        except Exception as e:
            logger.error(f"Error processing file: {e}")
            await update.message.reply_text(
                f"❌ An error occurred while encrypting your file:\n`{str(e)}`",
                parse_mode='Markdown'
            )
    
    async def handle_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        await update.message.reply_text(
            "📎 Please send me a Python file (.py) to encrypt!\n\n"
            "Use /help to see how to use this bot."
        )
    
    def run(self):
        """Start the bot"""
        # Create the Application
        application = Application.builder().token(self.token).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", self.start_command))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("about", self.about_command))
        
        # Add document handler for Python files
        application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))
        
        # Add text message handler
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_text))
        
        # Start the bot
        logger.info("🤖 Bot started successfully! Waiting for messages...")
        print("╔═══════════════════════════════════════════════════════╗")
        print("║     Python Encryptor Bot - Running Successfully                 ║")
        print("║              Powered by M0bsy                                   ║")
        print("╚═══════════════════════════════════════════════════════╝")
        print("\n✅ Bot is online and ready to encrypt Python files!")
        print("📱 Send Python files to your bot on Telegram")
        print("\nPress Ctrl+C to stop the bot\n")
        
        # Run the bot until the user presses Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES)

def main():
    # Get bot token from environment variable
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not bot_token:
        print("❌ ERROR: TELEGRAM_BOT_TOKEN not found!")
        print("\nPlease set your Telegram Bot Token:")
        print("1. Create a bot with @BotFather on Telegram")
        print("2. Get your bot token")
        print("3. Set it as environment variable: TELEGRAM_BOT_TOKEN")
        print("\nIn Termux:")
        print("  export TELEGRAM_BOT_TOKEN='your-token-here'")
        print("  python bot.py")
        sys.exit(1)
    
    # Create and run the bot
    bot = EncryptorBot(bot_token)
    bot.run()

if __name__ == "__main__":
    main()
