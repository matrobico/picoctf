# Wireshark doo dooo do doo...
> Forensics

### Description
> Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/d6f9aa16d2a2c51d2e431e658d87af9e/shark1.pcapng).
>
> **Hint 1: N/A**

### Solution
My first instinct when opening up this packet in wireshark was to do a string search for "pico*" to see if...

That didn't work (probably because I didn't perform the proper search) so I instead looked through all the HTTP traffic to see if I could find anything *not* encrypted and find the flag contained as data, or if I could find a GER request for the flag. Looking through the traffic, I found a unique packet that differed from the rest immediately preceeded by a GET request. Digging through this packet's data, it seemed the format of a flag was contained...

### Flag
`Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}cvpbPGS{c33xno00_1_f33_h_qrnqorrs}`
