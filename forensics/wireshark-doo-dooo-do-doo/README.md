# Wireshark doo dooo do doo...
> Forensics

### Description
> Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/d6f9aa16d2a2c51d2e431e658d87af9e/shark1.pcapng).
>
> **Hint 1: N/A**

### Solution
Opening up the given pcap within Wireshark displays a bunch of HTTP and TCP traffic. If we filter for only HTTP, we can see almost all packets contain encrypted data, minus a select few. Zeroing in on those select few, we can see that one of them contains what looks to be an encrypted flag:

`Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}`

At first I thought this data was encrypted by some key sent earlier in the capture, but in reality this was overthinking, and it's simply an encrypted flag sent over simple HTTP.

This encrypted flag is ROT13 encoded (determined by trying different ciphers), so decoding that reveals the plaintext flag.

### Flag
`picoCTF{p33kab00_1_s33_u_deadbeef}`
