"""
Simple AES-SIV encryption demo.
Uses PyCryptodome to provide nonce-misuse-resistant AEAD encryption.
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt(key: bytes, plaintext: bytes, associated_data: bytes = b""):
    """Encrypt with AES-SIV and return (ciphertext, tag)."""
    cipher = AES.new(key, AES.MODE_SIV)
    if associated_data:
        cipher.update(associated_data)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return ciphertext, tag


def decrypt(key: bytes, ciphertext: bytes, tag: bytes, associated_data: bytes = b""):
    """Decrypt AES-SIV ciphertext and verify integrity."""
    cipher = AES.new(key, AES.MODE_SIV)
    if associated_data:
        cipher.update(associated_data)
    return cipher.decrypt_and_verify(ciphertext, tag)


if __name__ == "__main__":
    # Generate random 256-bit key
    key = get_random_bytes(32)

    # Example message + associated data
    message = b"hello world, this is my secret text"
    ad = b"user:lokesh"

    # Encrypt
    ct, tag = encrypt(key, message, ad)
    print("Ciphertext:", ct.hex())
    print("Tag:", tag.hex())

    # Decrypt
    recovered = decrypt(key, ct, tag, ad)
    print("Recovered:", recovered.decode())


