AES-SIV is an authenticated encryption scheme that is nonce-misuse-resistant.
Unlike AES-GCM or ChaCha20-Poly1305, you don't require a distinct nonce each time — it's deterministic.

Here's how it works logically:

Inputs:

A secret key K (broken internally into two AES keys: one for MAC, one for CTR encryption).

The plaintext P (the message you're trying to protect).

Optional associated data AD (metadata you want authenticated but not encrypted).

Step 1: Compute a synthetic IV (SIV).

Run a MAC (CMAC/PMAC) over (AD, P) with half the key.

The output = a deterministic, cryptographically secure "IV".

This ensures: if (AD, P) is identical, you have the same IV → deterministic encryption.

Step 2: Encrypt with AES-CTR.

Use the synthetic IV as the counter seed.

Encrypt the plaintext using the other half of the key.

Outputs:

Ciphertext C

Authentication tag T (= the synthetic IV itself).

Decryption:

Recalculate the synthetic IV from (AD, C) and compare to T.

If equal → decrypt with AES-CTR and extract the plaintext.

If unequal → reject (integrity fail
