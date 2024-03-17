# interencdec (2024)
> Cryptography

### Description
> Can you get the real meaning from this file.
> 
> Download the file [here](https://artifacts.picoctf.net/c_titan/1/enc_flag).
>
> **Hint 1: Engaging in various decoding processes is of utmost importance**

### Solution
Taking a look at the file, we can see this contains a base64 encoded string. Decoding it reveals another base64 encoded string. Decoding that reveals yet another encoded string, but this time it appears to be a caesar shift (based on the first 2 letters shifted the same amount from "p" and "i"). Using cyberchef, we can see this is a rot19 which leads us to the flag.

The following python code can be used:
> import base64
> ct1 = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg=="
> ct2 = base64.b64decode(ct1)
> ct3 = base64.b64decode(ct2)
> ...

### Flag
`picoCTF{caesar_d3cr9pt3d_ea60e00b}`
