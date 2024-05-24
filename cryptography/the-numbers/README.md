# Warmed Up
> Cryptography

### Description
> The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?
>
>
> **Hint 1: The flag is in the format PICOCTF{}**

### Solution
There are 7 beginning numbers before the `{` character, which is how long "picoCTF" is. Furthermore, the first few numbers, if we use alphabet letter indexes, seem to translate to "picoCTF". So continuing to assume each number corresponds the same alphabet letter at that index, we get the solution.

### Flag
`PICOCTF{THENUMBERSMASON}`
