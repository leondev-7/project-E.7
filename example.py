# example.py
from siv_aead import encrypt, decrypt
from Crypto.Random import get_random_bytes


KEY = get_random_bytes(32)
AD = b"user:alice|purpose:backup"


message = b"top secret backup content\nkeep safe"
nonce, ct, tag = encrypt(KEY, message, AD)
print("Ciphertext hex:", ct.hex())


# simulation of storage/transport
pt = decrypt(KEY, nonce, ct, tag, AD)
print("Decrypted message:\n", pt.decode())
