# Super SSH (2024)
> General Skills

### Description
> Using a Secure Shell (SSH) is going to be pretty important.
>
> Can you ssh as ctf-player to titan.picoctf.net at port 55352 to get the flag?
>
> You'll also need the password 83dcefb7. If asked, accept the fingerprint with yes.
>
> If your device doesn't have a shell, you can use:
> https://webshell.picoctf.org
>
> If you're not sure what a shell is, check out our Primer:
> https://primer.picoctf.com/#_the_shell
>
> **Hint 1: **

### Solution
The solution is in the description. Just ssh with the following command:
> ssh ctf-player@titan.picoctf.net -p 55352

Then use the provided password to log in and retrieve the flag.

### Flag
`picoCTF{s3cur3_c0nn3ct10n_8969f7d3}`
