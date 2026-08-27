# -*- coding: utf-8 -*-
import sys
import math
import argparse
import os

def calculate_entropy(file_path):
    if not os.path.isfile(file_path):
        print(f"[-] Error: File '{file_path}' not found.")
        return 0.0
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    if not data:
        return 0.0
    
    byte_counts = [0] * 256
    for b in data:
        byte_counts[b] += 1
    
    total_bytes = len(data)
    entropy = 0.0
    
    for count in byte_counts:
        if count > 0:
            p = float(count) / total_bytes
            entropy -= p * math.log2(p)
            
    return entropy

def main():
    parser = argparse.ArgumentParser(description="HyperArmor-Skill Shannon Entropy Verifier")
    parser.add_argument("--file", "-f", required=True, help="Path to binary file (.exe, .dll, .so, .bin)")
    args = parser.parse_args()
    
    entropy = calculate_entropy(args.file)
    print("=" * 60)
    print(f"🛡️ HyperArmor Binary Shannon Entropy Analysis")
    print("=" * 60)
    print(f"Target File: {args.file}")
    print(f"Measured Entropy: {entropy:.4f} / 8.0000 bits per byte")
    
    if entropy >= 7.9000:
        print("[+] Defense Grade: S+ Tier (HyperArmor Physical Extreme Entropy)")
    elif entropy >= 7.2000:
        print("[+] Defense Grade: Standard Commercial Packed")
    else:
        print("[-] Defense Grade: Plaintext / Unprotected Binary")
    print("=" * 60)

if __name__ == '__main__':
    main()
