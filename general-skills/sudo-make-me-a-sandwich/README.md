# SUDO MAKE ME A SANDWICH
> General Skills

### Description
> Can you read the flag? I think you can!
>
> **Hint 1**: What is sudo?
>
> **Hint 2**: How do you know what permission you have?

### Solution
Connecting to the server, `flag.txt` is present but only accessible by root.

Running `sudo -l`, we can see what commands we're able to run as root. In this case, emacs is allowed. If we open `flag.txt` using emacs, we can see the flag.

### Flag
`picoCTF{ju57_5ud0_17_c2c0d2e2}`
