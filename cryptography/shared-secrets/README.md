# Shared Secrets
> Cryptography

### Description
> A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?
>
> **Hint 1**: What do you get if you combine a public key with a known private one?

### Solution
We're given 2 files:

1) message.txt
2) encryption.py

Opening `message.txt`, we can see a few variables the file seems to show as set: "a", "b", "g", "p", etc. These are all common variable names associated with the DH key exchange. This appear to be "leaked" values used in the DH algorithm. Additionally, `enc` appears to be the encoded message.

Opening `encryption.py`, this appears to be the recipe used to calculate everything.

Now, we should be able to just calculate the shared secret, then XOR that with every byte in enc to get the flag.


### Flag
`picoCTF{dh_s3cr3t_32ec2679}`
