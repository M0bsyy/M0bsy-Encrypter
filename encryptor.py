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
        self.encryption_layers = 5
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
    
    def xor_encrypt(self, data, key):
        """XOR encryption with key"""
        if isinstance(data, str):
            data = data.encode()
        if isinstance(key, str):
            key = key.encode()
        
        result = bytearray()
        key_len = len(key)
        for i, byte in enumerate(data):
            result.append(byte ^ key[i % key_len])
        return bytes(result)
    
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
        
        # LAYER 2: XOR encryption with random key
        xor_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        xor_encrypted = self.xor_encrypt(marshaled, xor_key)
        
        # LAYER 3: Zlib compression
        compressed = zlib.compress(xor_encrypted, 9)
        
        # LAYER 4: Base64 encoding
        b64_encoded = base64.b64encode(compressed)
        
        # LAYER 5: Hex encoding for additional obfuscation
        hex_encoded = b64_encoded.hex()
        
        # Generate random variable names for first layer decoder
        v1 = self.generate_random_var()
        v2 = self.generate_random_var()
        v3 = self.generate_random_var()
        v4 = self.generate_random_var()
        v5 = self.generate_random_var()
        v6 = self.generate_random_var()
        v7 = self.generate_random_var()
        v8 = self.generate_random_var()
        
        # Create layer 1 loader with XOR decryption
        layer1 = f"""import marshal, base64, zlib
{v1} = bytes.fromhex('{hex_encoded}')
{v2} = {repr(xor_key.encode())}
{v3} = base64.b64decode({v1})
{v4} = zlib.decompress({v3})
{v5} = bytearray()
for {v7}, {v8} in enumerate({v4}):
    {v5}.append({v8} ^ {v2}[{v7} % len({v2})])
{v6} = marshal.loads(bytes({v5}))
exec({v6})"""
        
        # Apply LAYER 2 of wrapping
        compiled_l2 = compile(layer1, '<string>', 'exec')
        marshaled_l2 = marshal.dumps(compiled_l2)
        compressed_l2 = zlib.compress(marshaled_l2, 9)
        encoded_l2 = base64.b64encode(compressed_l2)
        
        # Generate new variable names for layer 2
        w1 = self.generate_random_var()
        w2 = self.generate_random_var()
        w3 = self.generate_random_var()
        w4 = self.generate_random_var()
        
        layer2 = f"""import zlib, base64, marshal
{w1} = {repr(encoded_l2)}
{w2} = base64.b64decode({w1})
{w3} = zlib.decompress({w2})
{w4} = marshal.loads({w3})
exec({w4})"""
        
        # Apply LAYER 3 of wrapping
        compiled_l3 = compile(layer2, '<string>', 'exec')
        marshaled_l3 = marshal.dumps(compiled_l3)
        compressed_l3 = zlib.compress(marshaled_l3, 9)
        encoded_l3 = base64.b64encode(compressed_l3)
        hex_l3 = encoded_l3.hex()
        
        # Generate new variable names for layer 3
        x1 = self.generate_random_var()
        x2 = self.generate_random_var()
        x3 = self.generate_random_var()
        x4 = self.generate_random_var()
        x5 = self.generate_random_var()
        
        layer3 = f"""import zlib, base64, marshal
{x1} = bytes.fromhex('{hex_l3}')
{x2} = base64.b64decode({x1})
{x3} = zlib.decompress({x2})
{x4} = marshal.loads({x3})
exec({x4})"""
        
        # Apply LAYER 4 of wrapping with base85
        compiled_l4 = compile(layer3, '<string>', 'exec')
        marshaled_l4 = marshal.dumps(compiled_l4)
        compressed_l4 = zlib.compress(marshaled_l4, 9)
        encoded_l4 = base64.b85encode(compressed_l4)
        
        # Generate new variable names for layer 4
        y1 = self.generate_random_var()
        y2 = self.generate_random_var()
        y3 = self.generate_random_var()
        y4 = self.generate_random_var()
        
        layer4 = f"""import zlib, base64, marshal
{y1} = {repr(encoded_l4)}
{y2} = base64.b85decode({y1})
{y3} = zlib.decompress({y2})
{y4} = marshal.loads({y3})
exec({y4})"""
        
        # Apply FINAL LAYER 5 of wrapping
        compiled_l5 = compile(layer4, '<string>', 'exec')
        marshaled_l5 = marshal.dumps(compiled_l5)
        compressed_l5 = zlib.compress(marshaled_l5, 9)
        encoded_l5 = base64.b64encode(compressed_l5)
        
        # Generate junk code
        junk1 = self.generate_junk_code()
        junk2 = self.generate_junk_code()
        
        # Create branded header
        header = """#THIS ENCODE POWERED BY @M0bsy
# Multi-Layer Encryption System
# Encrypted with 5-Layer Advanced Obfuscation"""
        
        # Generate final obfuscated code with split execution
        z1 = self.generate_random_var()
        z2 = self.generate_random_var()
        z3 = self.generate_random_var()
        z4 = self.generate_random_var()
        z5 = self.generate_random_var()
        
        # Split the data into multiple parts for extra obfuscation
        part1 = encoded_l5[:len(encoded_l5)//3]
        part2 = encoded_l5[len(encoded_l5)//3:2*len(encoded_l5)//3]
        part3 = encoded_l5[2*len(encoded_l5)//3:]
        
        final_code = f"""{header}
# Encryption Layers: {self.encryption_layers} | XOR + Base64 + Base85 + Hex + Zlib + Marshal
import base64, marshal, zlib
{junk1}
{z1} = {repr(part1)}
{z2} = {repr(part2)}
{z3} = {repr(part3)}
{junk2}
{z4} = {z1} + {z2} + {z3}
{z5} = marshal.loads(zlib.decompress(base64.b64decode({z4})))
exec({z5})
"""
        
        return final_code

def print_banner():
    """Print tool banner"""
    banner = """
╔═══════════════════════════════════════════════════════╗
║     Python File Encryptor - Advanced Multi-Layer                ║
║         Ultra-Secure Code Obfuscation System                    ║
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
        print("  • 5 layers of advanced obfuscation")
        print("  • XOR encryption with random 32-char keys")
        print("  • Multiple encoding schemes (Base64, Base85, Hex)")
        print("  • Marshal bytecode compilation")
        print("  • Zlib compression (maximum level)")
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
