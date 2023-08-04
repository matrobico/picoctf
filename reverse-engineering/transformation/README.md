# Transformation
> Reverse Engineering

### Description
> I wonder what this really is...
>
> [enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc)
>
> ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]).
>
> **Hint 1: You may find some decoders online.**

### Solution
The challenge description gives us 2 things: a file named enc and a blob of python code. Looking at what's contained within the file shows us this:
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ
```
Interesting, a string of potentially Chinese characters. Is this the encoded flag? Let's put this aside for now and take a look at the blob of python code. 
Looking at the blob, it seems the each character of the flag is being converted to Unicode, left shifted 8 bits, then the character representation of that new Unicode value is taken. These characters are then all joined together into one string.
If we run the blob of python code with a random flag of our choosing, we can see some example output:
```
flag = "flag"
result = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
print(result)
>> 晬慧
```
It looks like the blob of python code is transforming the Unicode of the strings to Unicode values representing Chinese characters. Therefore, if we can take in the contents of the enc file and perform the reverse operations of what the code is doing, we should be able to retrieve the flag.

### Flag
`picoCTF{16_bits_inst34d_of_8_26684c20}`
