# Flag Hunters
> Reverse Engineering

### Description
> Lyrics jump from verses to the refrain kind of like a subroutine call. There's a hidden refrain this program doesn't print by default. Can you get it to print it? There might be something in it for you.
>
> **Hint 1**: This program can easily get into undefined states. Don't be shy about Ctrl-C.
>
> **Hint 2**: Unsanitized user input is always good, right?
>
> **Hint 3**: Is there any syntax that is ripe for subversion?

### Solution
There are 3 separate pieces of data to understanding the solution here:
- 1) The structure of the data
- 2) Where the vulnerability lies
- 3) How to trigger that vulnerability
- 4) The conditional statements used in printing the song lyrics

Firstly, the data here is an entire song contained in a variables. The flag is stored towards the beginning of that data.

Second, the vulnerability exists where user input is taken and stored into that same variable.

Third, we can see that data is then re-read, meaning that the part of the song buffer where the user inputted data is stored is re-read by the program (a few times actually).

And lastly, one of the conditionals is checking specifically for "RETURN [0-9]+", which is... odd. It's checking specifically for this string of characters, and then setting the lip to be whatever number is present.

So putting this all together, we just need to provide the proper input to trigger the program reading the flag from the beginning of the buffer. Since the lines are split by semicolons, if we use a ';' in our input, we can create a separate line with just "RETURN 0", which will then cause the program to jump to the flag portion of the lyrics.

### Flag
`picoCTF{70637h3r_f0r3v3r_a5202532}`
