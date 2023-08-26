# Easy Peasy
> Cryptography

### Description
> A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})
>
> `nc mercury.picoctf.net 20266` [otp.py](https://mercury.picoctf.net/static/84c434ada6e2f770b5000292cadae7eb/otp.py)
>
> **Hint 1: Maybe there's a way to make this a 2x pad.**

### Solution
Taking a look at `otp.py`, it seems that this binary uses a local key to encrypt a local flag. The length of the key 

### Flag
`picoCTF{99072996e6f7d397f6ea0128b4517c23}`
