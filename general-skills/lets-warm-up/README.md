# Lets Warm Up
> General Skills

### Description
> If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
>
> **Hint 1: Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

### Solution
This is just a simple hex to ascii conversion. We can use the following python code:

> byte_array = bytearray.fromhex("70")
> print(byte_array.decode('utf-8')

### Flag
`picoCTF{p}`
