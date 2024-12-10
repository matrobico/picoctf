# Collaborative Development
> General Skills

### Description
> My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?
>
> Additional details will be available after launching your challenge instance.
>
> [challenge.zip](https://artifacts.picoctf.net/c_titan/179/challenge.zip)

### Solution
Downloading and unzipping the provided file reveals a single directory containing `flag.py` and a hidden `.git` directory. Checking the `.git/logs/refs/heads` directory, we can see different commits for the "features" branch, so it's clear that we'll have to checkout different "features" of this git repo to see the different parts of the flag.

Checkout out `features/part-1`, `features/part-2`, and `features/part-3` reveals the full flag.

### Flag
`picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_798f9981}`
