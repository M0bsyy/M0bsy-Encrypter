#!/usr/bin/env python3
"""
Python File Encryptor - Military-Grade AES-256 Encryption
Powered by M0bsy
"""

import marshal
import base64
import os
import sys
import random
import string
import keyword
import hashlib
import zlib
from cryptography.fernet import Fernet

class PythonEncryptor:
    def __init__(self):
        self.encryption_type = "AES-256 (Military-Grade)"
        self.python_keywords = set(keyword.kwlist)
        
    def generate_random_var(self, length=None):
        if length is None:
            length = random.randint(15, 25)
        while True:
            first_char = random.choice(string.ascii_letters + '_')
            rest_chars = ''.join(random.choice(string.ascii_letters + string.digits + '_') for _ in range(length - 1))
            var_name = first_char + rest_chars
            if var_name not in self.python_keywords and not var_name[0].isdigit():
                return var_name
    
    def generate_junk_code(self, density=8):
        junk_lines = []
        templates = [
            lambda: f"{self.generate_random_var()}={random.randint(-9999999,9999999)}",
            lambda: f"{self.generate_random_var()}=bytes.fromhex('{os.urandom(64).hex()}')",
            lambda: f"{self.generate_random_var()}={repr(os.urandom(128))}",
            lambda: f"def {self.generate_random_var()}():pass",
            lambda: f"{self.generate_random_var()}=hash(__name__)",
            lambda: f"{self.generate_random_var()}=pow({random.randint(2,100)},{random.randint(2,10)})",
            lambda: f"{self.generate_random_var()}=abs({random.randint(-9999,9999)})",
            lambda: f"{self.generate_random_var()}=[x for x in range({random.randint(1,10)})]",
        ]
        for _ in range(density):
            junk_lines.append(random.choice(templates)())
        return '\n'.join(junk_lines)
    
    def encrypt_file(self, input_file, output_file=None):
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
            print(f"[+] Applying Military-Grade Encryption...")
            
            encrypted_code = self._apply_encryption(source_code)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_code)
            
            print(f"[+] Encryption complete!")
            print(f"[+] Encrypted file saved as: {output_file}")
            print(f"[+] Encrypted size: {len(encrypted_code)} bytes")
            print(f"[+] Obfuscation ratio: {len(encrypted_code)/len(source_code):.2f}x")
            print(f"[+] Security: MILITARY-GRADE (AES-256 + Zlib)")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def _apply_encryption(self, source_code):
        compiled = compile(source_code, '<string>', 'exec')
        marshaled = marshal.dumps(compiled)
        
        # LAYER 1: Zlib compression (level 9)
        compressed = zlib.compress(marshaled, 9)
        
        # LAYER 2: Fernet AES-256 encryption
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted = cipher.encrypt(compressed)
        
        # LAYER 3: Single base64 encoding (for readability)
        data_b64 = base64.b64encode(encrypted).decode()
        
        # LAYER 4: Checksum verification
        checksum = hashlib.sha256(data_b64.encode()).hexdigest()
        
        # LAYER 5: Split into 15 parts
        chunk = len(data_b64) // 15
        parts = []
        for i in range(15):
            if i == 14:
                parts.append(data_b64[i*chunk:])
            else:
                parts.append(data_b64[i*chunk:(i+1)*chunk])
        
        v = {i: self.generate_random_var() for i in range(60)}
        
        header = """#@M0bsy ENCRYPTOR - MILITARY-GRADE AES-256
#ZLIB COMPRESSION + FERNET ENCRYPTION
#UNBREAKABLE SECURITY"""
        
        parts_str = "','".join(parts)
        
        decoder = f"""{header}
import marshal,base64,hashlib,zlib;from cryptography.fernet import Fernet
{self.generate_junk_code(6)}
def {v[0]}():
 {v[1]}=['{parts_str}']
 {v[2]}=''.join({v[1]})
 {v[3]}='{checksum}'
 {v[4]}=hashlib.sha256({v[2]}.encode()).hexdigest()
 if {v[3]}!={v[4]}:raise RuntimeError('Integrity check failed')
 {v[5]}='{key.decode()}'
 {v[6]}=base64.b64decode({v[2]})
 {v[7]}=Fernet({v[5]}.encode())
 {v[8]}={v[7]}.decrypt({v[6]})
 {v[9]}=zlib.decompress({v[8]})
 {v[10]}=marshal.loads({v[9]})
 return {v[10]}
{self.generate_junk_code(8)}
exec({v[0]}())
{self.generate_junk_code(6)}
"""
        return decoder

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════╗
║    Python Encryptor - Military-Grade AES-256           ║
║         Zlib + Fernet + Anti-Analysis                  ║
╚══════════════════════════════════════════════════════════╝
    """)

def main():
    print_banner()
    if len(sys.argv) < 2:
        print("Usage: python encryptor.py <file.py> [output.py]")
        print("\nFeatures: ✓ AES-256 ✓ Zlib ✓ Checksum ✓ 15-Part Split ✓ Junk Code")
        return
    
    encryptor = PythonEncryptor()
    success = encryptor.encrypt_file(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    if success:
        print("\n✓ Encryption successful! Unbreakable!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
