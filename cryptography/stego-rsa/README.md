# StegoRSA
> Cryptography

### Description
> A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message?
>
> **Hint 1**: Metadata can tell you more than you expect.
>
> **Hint 2**: Hex can be turned back into a key file.

### Solution
The solution provides both an image and an encrypted flag file.

Using `exiftool`, we can see the private key is left as a comment. Why is this the case? Who knows, it seems it's simply a gimic of the challenge.

Taking the value of the image's comment, we have what looks to be a long string of hex. We can reverse this using xxd to get original byte values of the key, rather than a hex representation. The following command is basically saying "take the hex string, interpret it as plain hex, and reverse it". Without the `-p`, `xxd` would assume the input the typical hex format of `xxd` and output nothing.

`cat key | xxd -r -p > recovered_key`

Now we have:

1) The key file
2) The encrypted data

Which means we can use `openssl` to take care of the rest, as it's the defacto CMDLINE tool for dealing with crypto operations. The following command should work:

`openssl pkeyutl -decrypt -inkey recovered_key -in flag.enc -out flag`

Where:

- openssl - the command
- pkeyutl - public key utility for handling public/private key operations
- decrypt - decode the key
- inkey - our private key to use
- in - the encrypted data we're providing as input

### Flag
`picoCTF{rs4_k3y_1n_1mg_ce170c3d}`
