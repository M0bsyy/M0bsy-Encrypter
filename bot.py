#!/usr/bin/env python3
"""
Python File Encryptor - Advanced Multi-Layer Obfuscation Tool
This tool encrypts Python files using multiple layers of advanced obfuscation
while keeping them executable.
"""

import marshal
import base64
import zlib
import os
import sys
import random
import string
import keyword

class PythonEncryptor:
    def __init__(self):
        self.encryption_layers = 3
        self.python_keywords = set(keyword.kwlist)
        
    def generate_random_var(self, length=None):
        """Generate random variable names for obfuscation, avoiding Python keywords"""
        if length is None:
            length = random.randint(8, 16)
        
        while True:
            first_char = random.choice(string.ascii_letters + '_')
            rest_chars = ''.join(random.choice(string.ascii_letters + string.digits + '_') for _ in range(length - 1))
            var_name = first_char + rest_chars
            
            if var_name not in self.python_keywords and not var_name[0].isdigit():
                return var_name
    
    def generate_junk_code(self):
        """Generate junk code to confuse reverse engineers"""
        junk_templates = [
            f"{self.generate_random_var()} = {random.randint(1000, 9999)}",
            f"{self.generate_random_var()} = '{self.generate_random_var()}'",
            f"{self.generate_random_var()} = lambda x: x * {random.randint(1, 10)}",
            f"_ = {random.randint(100, 999)} + {random.randint(100, 999)}",
        ]
        return '\n'.join(random.sample(junk_templates, random.randint(2, 4)))
    
    def encrypt_file(self, input_file, output_file=None):
        """
        Encrypt a Python file with multi-layer obfuscation
        """
        if not os.path.exists(input_file):
            print(f"Error: File '{input_file}' not found!")
            return False
        
        if output_file is None:
            base_name = os.path.basename(input_file)
            output_file = f"encrypted_{base_name}"
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                source_code = f.read()
            
            print(f"[+] Reading file: {input_file}")
            print(f"[+] Original size: {len(source_code)} bytes")
            print(f"[+] Applying {self.encryption_layers} layers of encryption...")
            
            encrypted_code = self._apply_encryption(source_code)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_code)
            
            print(f"[+] Encryption complete!")
            print(f"[+] Encrypted file saved as: {output_file}")
            print(f"[+] Encrypted size: {len(encrypted_code)} bytes")
            print(f"[+] Obfuscation ratio: {len(encrypted_code)/len(source_code):.2f}x")
            
            return True
            
        except Exception as e:
            print(f"Error during encryption: {e}")
            return False
    
    def _apply_encryption(self, source_code):
        """Apply multiple layers of advanced encryption"""
        
        # LAYER 1: Compile and marshal
        compiled_code = compile(source_code, '<string>', 'exec')
        marshaled = marshal.dumps(compiled_code)
        
        # LAYER 2: Zlib compression (level 9)
        compressed = zlib.compress(marshaled, 9)
        
        # LAYER 3: Base64 encoding
        encoded = base64.b64encode(compressed).decode('ascii')
        
        # Generate random variable names
        v1 = self.generate_random_var()
        v2 = self.generate_random_var()
        v3 = self.generate_random_var()
        v4 = self.generate_random_var()
        
        # Generate junk code
        junk1 = self.generate_junk_code()
        junk2 = self.generate_junk_code()
        
        # Create branded header
        header = """#THIS ENCODE POWERED BY @M0bsy
# Multi-Layer Encryption System
# Encrypted with 3-Layer Advanced Obfuscation"""
        
        # Split data into 3 parts for additional obfuscation
        part_size = len(encoded) // 3
        part1 = encoded[:part_size]
        part2 = encoded[part_size:2*part_size]
        part3 = encoded[2*part_size:]
        
        # Create final obfuscated code
        final_code = f"""{header}
import base64, marshal, zlib
{junk1}
{v1} = '{part1}'
{v2} = '{part2}'
{v3} = '{part3}'
{junk2}
{v4} = base64.b64decode(({v1}+{v2}+{v3}).encode())
exec(marshal.loads(zlib.decompress({v4})))
"""
        
        return final_code

def print_banner():
    """Print tool banner"""
    banner = """
╔═══════════════════════════════════════════════════════╗
║     Python File Encryptor - Advanced Multi-Layer      ║
║         Ultra-Secure Code Obfuscation System          ║
╚═══════════════════════════════════════════════════════╝
    """
    print(banner)

def main():
    print_banner()
    
    if len(sys.argv) < 2:
        print("Usage: python encryptor.py <input_file.py> [output_file.py]")
        print("\nExample:")
        print("  python encryptor.py myfile.py")
        print("  python encryptor.py myfile.py encrypted_myfile.py")
        print("\nFeatures:")
        print("  • 3 layers of advanced obfuscation")
        print("  • Marshal bytecode compilation")
        print("  • Zlib compression (maximum level)")
        print("  • Base64 encoding")
        print("  • Random variable name obfuscation")
        print("  • Junk code injection")
        print("  • Split data execution")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    encryptor = PythonEncryptor()
    success = encryptor.encrypt_file(input_file, output_file)
    
    if success:
        print("\n✓ Encryption successful!")
        print("  Your file is now protected with advanced multi-layer encryption.")
        print("  Run it like any normal Python file.")
        print("  Extremely difficult to reverse engineer!")
    else:
        print("\n✗ Encryption failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
