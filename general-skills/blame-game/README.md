# Blame Game
> General Skills

### Description
> Someone's commits seems to be preventing the program from working. Who is it?
>
> You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_titan/72/challenge.zip)
>
> **Hint 1**: In collaborative projects, many users can make many changes. How can you see the changes within one file?
>
> **Hint 2**: Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control).
>
> **Hint 3**: You can use python3 <file>.py to try running the code, though you won't need to for this challenge.

### Solution
The zip file provided to us contains a git folder with a single python file. Running `git log` to show the commit history immediately presents us with the flag - the author of the second commit. Running `git show <commit-id>` on that commit shows that this was indeed the commit that introduced an error into the python print statement.

### Flag
`picoCTF{@sk_th3_1nt3rn_b64c4705}`
