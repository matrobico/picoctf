# Piece By Piece
> General Skills

### Description
> After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.
>
> **Hint 1**: 

### Solution
A larger zip file had been split using `split`.

```
cat part* > restored_zip.zip
unzip restored_zip.zip
cat flag.txt
```

### Flag
`picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_4e5c49a8}`
