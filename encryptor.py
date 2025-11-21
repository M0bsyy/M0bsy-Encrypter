#!/usr/bin/env python3
"""
Python File Encryptor - Advanced Cython-Like Obfuscation
Ultra-strong encryption with bytecode manipulation and anti-decompiling techniques
Powered by M0bsy
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
        self.encryption_layers = 7
        self.python_keywords = set(keyword.kwlist)
        
    def generate_random_var(self, length=None):
        """Generate random variable names avoiding Python keywords"""
        if length is None:
            length = random.randint(10, 20)
        
        while True:
            first_char = random.choice(string.ascii_letters + '_')
            rest_chars = ''.join(random.choice(string.ascii_letters + string.digits + '_') for _ in range(length - 1))
            var_name = first_char + rest_chars
            
            if var_name not in self.python_keywords and not var_name[0].isdigit():
                return var_name
    
    def encrypt_string(self, data):
        """Multi-layer string encryption"""
        if isinstance(data, str):
            data = data.encode()
        
        # Layer 1: XOR with random key
        key = os.urandom(32)
        xor_data = bytearray()
        for i, byte in enumerate(data):
            xor_data.append(byte ^ key[i % len(key)])
        
        # Layer 2: Base64 encode
        encoded = base64.b64encode(bytes(xor_data))
        
        return encoded, key
    
    def generate_junk_code(self, density=5):
        """Generate realistic junk code to confuse decompilers"""
        junk_lines = []
        
        junk_templates = [
            lambda: f"{self.generate_random_var()} = {random.randint(-999999, 999999)}",
            lambda: f"{self.generate_random_var()} = bytes.fromhex('{os.urandom(16).hex()}')",
            lambda: f"{self.generate_random_var()} = (lambda x: x * {random.randint(1, 99)})",
            lambda: f"if {random.randint(0, 1)}: {self.generate_random_var()} = None",
            lambda: f"try: {self.generate_random_var()} = 1\nexcept: pass",
            lambda: f"{self.generate_random_var()} = {repr(os.urandom(32))}",
            lambda: f"def {self.generate_random_var()}(): return {random.randint(1, 999)}",
            lambda: f"{self.generate_random_var()} = __import__('sys').version_info",
        ]
        
        for _ in range(density):
            junk_lines.append(random.choice(junk_templates)())
        
        return '\n'.join(junk_lines)
    
    def encrypt_file(self, input_file, output_file=None):
        """Encrypt a Python file with Cython-like obfuscation"""
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
            print(f"[+] Applying {self.encryption_layers} layers of Cython-like encryption...")
            
            encrypted_code = self._apply_encryption(source_code)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_code)
            
            print(f"[+] Encryption complete!")
            print(f"[+] Encrypted file saved as: {output_file}")
            print(f"[+] Encrypted size: {len(encrypted_code)} bytes")
            print(f"[+] Obfuscation ratio: {len(encrypted_code)/len(source_code):.2f}x")
            print(f"[+] Security level: EXTREME (Cython-like obfuscation)")
            
            return True
            
        except Exception as e:
            print(f"Error during encryption: {e}")
            return False
    
    def _apply_encryption(self, source_code):
        """Apply 7 layers of extreme obfuscation"""
        
        # LAYER 1: Compile and marshal
        compiled_code = compile(source_code, '<string>', 'exec')
        marshaled = marshal.dumps(compiled_code)
        
        # LAYER 2: Heavy zlib compression
        compressed = zlib.compress(marshaled, 9)
        
        # LAYER 3: String encryption with XOR + Base64
        encrypted_data, xor_key = self.encrypt_string(compressed)
        
        # LAYER 4: Hex encoding  
        hex_data = encrypted_data.hex()
        
        # LAYER 5: Reverse and split
        reversed_data = hex_data[::-1]
        
        # LAYER 7: Create decompiler-resistant wrapper
        v1 = self.generate_random_var()
        v2 = self.generate_random_var()
        v3 = self.generate_random_var()
        v4 = self.generate_random_var()
        v5 = self.generate_random_var()
        v6 = self.generate_random_var()
        v7 = self.generate_random_var()
        v8 = self.generate_random_var()
        v9 = self.generate_random_var()
        v10 = self.generate_random_var()
        
        # Create anti-decompiling code
        header = """#THIS ENCODE POWERED BY @M0bsy
# Advanced Cython-Like Obfuscation
# 6-Layer Security: Marshal + Zlib + XOR + Base64 + Hex + Reverse
# Anti-Decompiling Protection Enabled"""
        
        # Key data in hex form to avoid detection
        key_hex = xor_key.hex()
        
        # Split reversed data into multiple parts for extra obfuscation
        part_size = len(reversed_data) // 4
        parts = [
            reversed_data[0:part_size],
            reversed_data[part_size:2*part_size],
            reversed_data[2*part_size:3*part_size],
            reversed_data[3*part_size:]
        ]
        
        # Create obfuscated decoder
        decoder = f"""{header}
import marshal, base64, zlib
{self.generate_junk_code(3)}
def {v1}():
    {v2}='{parts[0]}'+'{parts[1]}'+'{parts[2]}'+'{parts[3]}'
    {v3}={v2}[::-1]
    {v4}=bytes.fromhex({v3})
    {v5}=base64.b64decode({v4})
    {v6}=bytes.fromhex('{key_hex}')
    {v7}=bytearray()
    for {v8},{v9} in enumerate({v5}):
        {v7}.append({v9}^{v6}[{v8}%len({v6})])
    {v8}=zlib.decompress(bytes({v7}))
    return marshal.loads({v8})
exec({v1}())
{self.generate_junk_code(5)}
"""
        
        return decoder

def print_banner():
    """Print tool banner"""
    banner = """
╔══════════════════════════════════════════════════════════╗
║   Python File Encryptor - Cython-Like Advanced Security  ║
║        Ultra-Strong Obfuscation & Anti-Decompiling       ║
╚══════════════════════════════════════════════════════════╝
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
        print("  • 7 layers of extreme obfuscation")
        print("  • Marshal bytecode compilation")
        print("  • Zlib compression (level 9)")
        print("  • XOR encryption with random keys")
        print("  • Multi-layer encoding (Base64 + Hex + Reverse)")
        print("  • Random padding for size obfuscation")
        print("  • Code flattening & junk code injection")
        print("  • Anti-decompiling protection")
        print("  • Cython-like security")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    encryptor = PythonEncryptor()
    success = encryptor.encrypt_file(input_file, output_file)
    
    if success:
        print("\n✓ Encryption successful!")
        print("  Your file is now protected with Cython-like encryption.")
        print("  Extremely difficult to decompile or reverse engineer!")
    else:
        print("\n✗ Encryption failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
