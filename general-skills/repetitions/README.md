# Repetitions
> General Skills

### Description
> Can you make sense of this file?
>
> Download the file [here](https://artifacts.picoctf.net/c/473/enc_flag).
>
> **Hint 1:** Multiple decoding is always good.

### Solution
Opening the provided file reveals a base64 encoded string. Decoding this reveals another base64 decoded string, and so on until you hit the flag.

### Flag
`picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dfe803c6}`
