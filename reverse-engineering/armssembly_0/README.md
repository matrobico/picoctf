# Magikarp Ground Mission
> General Skills

### Description
> What integer does this program print with arguments `182476535` and `3742084308`? File: [chall.S](https://mercury.picoctf.net/static/39820b71cabc14033bca1f2db00a6801/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
>
> Additional details will be available after launching your challenge instance.
>
> **Hint 1: Finding a cheatsheet for bash would be really helpful!**

### Solution
Opening up `chall.S`, we can see that it is filled with `ARMv8-a` ISA assembly code. Therefore, [this](https://diveintosystems.org/book/C9-ARM64/index.html) or [this](https://developer.arm.com/documentation/den0024/a/The-A64-instruction-set?lang=en) document should prove useful in understanding the instructions.

The use of registers prefixed with `x` means that this is AARCH 64, not 32

Further

### Flag
