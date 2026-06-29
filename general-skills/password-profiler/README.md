# Password Profiler
> General Skills

### Description
> We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. Using OSINT techniques, you are provided with personal details about the target. Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash.
>
>
> [userinfo](https://challenge-files.picoctf.net/c_plain_mesa/3c16fb8e48ddae444f6840e81660a5a8cb2d30b69092b04f619d6ac34676a919/userinfo.txt): Contains the personal details.
>
> [hash](https://challenge-files.picoctf.net/c_plain_mesa/3c16fb8e48ddae444f6840e81660a5a8cb2d30b69092b04f619d6ac34676a919/hash.txt): Contains the SHA-1 hash of the password.
>
> [check_password](https://challenge-files.picoctf.net/c_plain_mesa/3c16fb8e48ddae444f6840e81660a5a8cb2d30b69092b04f619d6ac34676a919/check_password.py): Script to test passwords against the hash.
>
> **Hint 1**: [CUPP](https://github.com/Mebus/cupp) is a Python tool for generating custom wordlists from personal data.

### Solution
Run CUPP and supply it with the user info. Then take the generated output, store it as `passwords.txt` and run the provided `check_password.py` script to crack the SHA-1 hash.

### Flag
`picoCTF{Aj_15901990}`
