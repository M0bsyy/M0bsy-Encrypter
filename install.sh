#!/bin/bash

echo "╔═══════════════════════════════════════════════════════╗"
echo "║     Python File Encryptor - Installation Script      ║"
echo "║              Powered by M0bsy                         ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3 first."
    exit 1
fi

echo "✅ Python 3 found!"
python3 --version
echo ""

# Install python-telegram-bot
echo "📦 Installing python-telegram-bot library..."
pip install python-telegram-bot

if [ $? -eq 0 ]; then
    echo ""
    echo "╔═══════════════════════════════════════════════════════╗"
    echo "║            Installation Complete! ✅                  ║"
    echo "╚═══════════════════════════════════════════════════════╝"
    echo ""
    echo "📚 Quick Start Guide:"
    echo ""
    echo "1️⃣  METHOD 1: Using Telegram Bot (Recommended)"
    echo "   Get your bot token from @BotFather on Telegram"
    echo "   Then run:"
    echo ""
    echo "   export TELEGRAM_BOT_TOKEN='your-token-here'"
    echo "   python3 bot.py"
    echo ""
    echo "2️⃣  METHOD 2: Command Line Encryption"
    echo "   python3 encryptor.py sample.py"
    echo "   python3 encrypted_sample.py"
    echo ""
    echo "💡 Test the sample file:"
    echo "   python3 sample.py"
    echo ""
else
    echo ""
    echo "❌ Installation failed!"
    echo "Try running: pip install --upgrade python-telegram-bot"
    exit 1
fi
