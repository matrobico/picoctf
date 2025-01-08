# Big Zip
> General Skills

### Description
> Unzip this archive and find the flag.
>
> [Download the zip file](https://artifacts.picoctf.net/c/504/big-zip-files.zip).
>
> **Hint 1:** Can grep be instructed to look at every file in a directory and its subdirectories?

### Solution
As the name of this problem states, we're given a large zip file with many directories. Simply using `grep` with `-r` allows us to recursively look for the flag (e.g., `grep -rI 'pico'`).

### Flag
`picoCTF{gr3p_15_m4g1c_ef8790dc}`
