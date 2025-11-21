# Python File Encryptor
### Powered by M0bsy 🔥

An advanced Python obfuscation tool that encrypts Python files using **5 layers** of ultra-secure encoding while keeping them fully executable.

**✨ NEW: Telegram Bot Support!** Now includes an automated Telegram bot that encrypts files instantly!

## Features

- **5 Layers of Advanced Obfuscation**:
  - **XOR encryption** with random 32-character keys
  - **Marshal** bytecode compilation
  - **Zlib** compression (maximum level 9)
  - **Base64** and **Base85** encoding
  - **Hex** encoding for additional security
  - Random variable name obfuscation (keyword-safe)
  - Junk code injection
  - Split data execution
  
- **Ultra-Secure**: 7-8x larger encrypted files, extremely difficult to reverse engineer
- **Executable After Encryption**: Encrypted files run exactly like the original
- **Command-Line Interface**: Easy to use from terminal
- **Preserves Functionality**: All features of original file work after encryption

## How It Works

The advanced obfuscation process applies **5 nested layers**:

1. **Layer 1**: Compiles source code to bytecode using `marshal`
2. **Layer 2**: Applies XOR encryption with random 32-character key
3. **Layer 3**: Compresses with `zlib` (level 9)
4. **Layer 4**: Encodes with Base64 and Hex
5. **Layer 5**: Wraps with Base85 encoding
6. **Additional**: Random variable names, junk code injection, split data execution

Each layer is nested inside the next, creating an extremely complex obfuscation that's very difficult to reverse engineer.

## Usage

### Method 1: Telegram Bot (Recommended for Mobile) 📱

The easiest way to encrypt files on the go! Just send Python files to your Telegram bot.

#### Setup Telegram Bot:

1. **Create your bot:**
   - Open Telegram and find **@BotFather**
   - Send `/newbot` command
   - Choose a name and username for your bot
   - Copy the **bot token** you receive

2. **Run the bot in Termux:**
   ```bash
   # Set your bot token (replace with your actual token)
   export TELEGRAM_BOT_TOKEN='1234567890:ABCdefGHIjklMNOpqrsTUVwxyz'
   
   # Start the bot
   python bot.py
