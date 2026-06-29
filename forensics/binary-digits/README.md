# Binary Digits
> Forensics

### Description
> This file doesn't look like much... just a bunch of 1s and 0s. But maybe it's not just random noise. Can you recover anything meaningful from this?
>
> Download the file [here](https://challenge-files.picoctf.net/c_plain_mesa/fc041c019da080f2d57c4f5e082de1f34261258b063e3c2cc6e42808b30463f9/digits.bin).

### Solution
The file is in binary. We can use CyberChef to decode it, then seeing as there a "JFIF" in the header, we can output to .jpg and view the image, which shows the flag.

### Flag
`picoCTF{h1dd3n_1n_th3_b1n4ry_2f96e9a1}`
