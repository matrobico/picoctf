# Commitment Issues (2024)
> General Skills

### Description
> I accidentally wrote the flag down. Good thing I deleted it!
> 
> You download the challenge files here:
> [challenge.zip](challenge.zip)
>
> **Hint 1: Version control can help you recover files if you change or lose them!**
> **Hint 2: Read the chapter on Git from the picoPrimer [here](https://primer.picoctf.org/#_git_version_control)**
> **Hint 3: You can 'checkout' commits to see the files inside them**

### Solution
We're given a zip file containing a message file displaying "TOP SECRET" and a hidden git directory. What's likely the case (based on what's in the zip and the name of this challenge) is we'll have to use some git command to retreive a previous git commit where the flag was visible. The trick will be to figure out what commit and how to retrieve it.

Using `git log`, we can see the commit where the flag was created. Then, using `git checkout COMMIT_ID`, we can checkout the commit before the flag was removed. The flag can then be found in `message.txt`.

### Flag
`picoCTF{s@n1t1z3_9539be6b}`
