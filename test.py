# test_siv.py
import pytest
from siv_aead import encrypt, decrypt
from Crypto.Random import get_random_bytes




def test_encrypt_decrypt_roundtrip():
key = get_random_bytes(32)
ad = b"meta"
pt = b"hello world"
nonce, ct, tag = encrypt(key, pt, ad)
out = decrypt(key, nonce, ct, tag, ad)
assert out == pt




def test_tamper_detects():
key = get_random_bytes(32)
ad = b"meta"
pt = b"hello"
nonce, ct, tag = encrypt(key, pt, ad)
# flip a byte in ciphertext
bad = bytearray(ct)
bad[0] ^= 1
with pytest.raises(ValueError):
decrypt(key, nonce, bytes(bad), tag, ad)




def test_ad_mismatch_detects():
key = get_random_bytes(32)
ad = b"meta"
pt = b"hello"
nonce, ct, tag = encrypt(key, pt, ad)
with pytest.raises(ValueError):
decrypt(key, nonce, ct, tag, b"different")
