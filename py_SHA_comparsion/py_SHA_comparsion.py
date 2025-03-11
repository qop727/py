# Program to compare SHA hash code of a file and input.

import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()                  # Calculate the SHA-256 checksum of a file.
    try:
        with open(file_path, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"\nChyba: Soubor nenalezen - {file_path}")
        return None

def compare_checksum(file_path, provided_checksum):
    file_checksum = calculate_sha256(file_path)     # Compare the SHA-256 checksum of a file with a provided checksum.
    if file_checksum is None:
        return False
    return file_checksum == provided_checksum

# Input file path and the SHA-256 hash to compare
file_path = input("Zadejte, prosím, kompletní cestu k souboru: ")
provided_checksum = input("Zadejte, prosím, SHA-256 hash kód k porovnání: ")
print("\nPorovnávám, prosím čekejte...")

# Compare checksums
if compare_checksum(file_path, provided_checksum):
    print("\nSHA-256 checksum souboru JE stejný, jako zadaný hash kód!")
else:
    print("\nSHA-256 checksum souboru NENÍ stejný, jako zadaný hash kód!")

# Wait for the user to press Enter before exiting
input("\nPro ukončení programu stiskněte Enter...")