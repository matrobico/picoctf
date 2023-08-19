# Easy Peasy
> Cryptography

### Description
> A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})
>
> `nc mercury.picoctf.net 20266` [otp.py](https://mercury.picoctf.net/static/84c434ada6e2f770b5000292cadae7eb/otp.py)
>
> **Hint 1: Maybe there's a way to make this a 2x pad.**

### Solution
Need another ciphertext of any message, but using the same key portion. Two ciphertexts of the same key is known as Two-Time Pad and can be used to break encryption.

To get a message of my choosing encrypted with the same key portion, I need to feed enough input to get the key to cycle back to the beginning (code cycles key use).

Need to feet up to 5000, so it cycles back to a start index of 0, then 

### Flag
`picoCTF{99072996e6f7d397f6ea0128b4517c23}`
