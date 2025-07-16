# One-Time-Pad

The one-time pad (OTP) is an encryption technique that cannot be cracked in cryptography. It requires the use of a single-use pre-shared key that is equal to the size of the message being sent. In OTP, a plaintext is paired with a random secret key (also referred to as a one-time pad). Then, each bit or character of the plaintext is encrypted by combining it with the corresponding bit or character from the pad using modular addition.

The resulting ciphertext is impossible to break if the following four conditions are met:
- The key must be at least as long as the plaintext.
- The key must be truly random.
- The key must never be reused in whole or in part.
- The key must be kept completely secret by the communicating parties.

These requirements make the OTP the only known encryption system that is mathematically proven to be unbreakable under the principles of information theory. - [Wikipedia](https://en.wikipedia.org/wiki/One-time_pad)

# Usage
Run 
```bash
python3 main.py
```

Choose mode, and enter your plaintext or ciphertext, and the key. You can enter the keys inside the program (safest), or pass the data on the commandline.
For more information on how to use commandline options, run:
```bash
python3 main.py --help
```
