#!/bin/bash

echo "╔═══════════════════════════════════════════════════════╗"
echo "║        Checking Required Files - M0bsy Encryptor     ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

FILES=(
    "encryptor.py"
    "bot.py"
    "sample.py"
    "README.md"
    ".gitignore"
    "install.sh"
    "requirements.txt"
)

MISSING=0

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file - MISSING!"
        MISSING=$((MISSING + 1))
    fi
done

echo ""
if [ $MISSING -eq 0 ]; then
    echo "╔═══════════════════════════════════════════════════════╗"
    echo "║      ✅ All files present! Ready for GitHub!         ║"
    echo "╚═══════════════════════════════════════════════════════╝"
else
    echo "❌ Missing $MISSING file(s)!"
fi
