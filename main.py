import os
import argparse
import string

ALPHABET = string.ascii_uppercase + string.ascii_lowercase + " "

def encrypt(plaintext: str, key: str) -> str:
    ciphertext = ""
    for i in range(len(plaintext)):
        p = ALPHABET.index(plaintext[i])
        k = ALPHABET.index(key[i])
        c = (p + k) % len(ALPHABET)
        ciphertext += ALPHABET[c]
    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    decrypted = ""
    for i in range(len(ciphertext)):
        c = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[i])
        p = (c - k + len(ALPHABET)) % len(ALPHABET)
        decrypted += ALPHABET[p]
    return decrypted

def main(mode: str, text: str, key: str) -> None:
    mode = args.mode if args.mode else input("Enter mode [decrypt / encrypt]: ")
    if mode.lower() in ["encrypt", "enc", "e"]:
        mode = True
    elif mode.lower() in ["decrypt", "dec", "d"]:
        mode = False
    else:
        raise ValueError("Unknown mode of operation!")

    text = args.msg if args.msg else input("Enter plaintext: " if mode else "Enter ciphertext: ")
    key  = args.key if args.key else input("Enter key: ")

    if len(text) != len(key):
        raise ValueError("Input and key lengths MUST match!")

    if mode:
        print("Ciphertext:", encrypt(text, key))
    else:
        print("Plaintext:", decrypt(text, key))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "Simple One-Time-Pad encryption and decryption tool"
    )

    parser.add_argument("--mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("--msg", help="The message (A-Z only, no spaces)")
    parser.add_argument("--key", help="The one-time pad (same length as message)")

    args = parser.parse_args()
    try:
        main(args.mode, args.msg, args.key)
    except ValueError as e:
        print(e)
        os._exit(1)

