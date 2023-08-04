# Transformation
> Reverse Engineering

### Description
> I wonder what this really is...
> [enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc)
> ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]).
> **Hint 1: You may find some decoders online.**

### Solution
