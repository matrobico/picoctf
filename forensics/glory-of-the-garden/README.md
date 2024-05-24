# Glory of the Garden
> Forensics

### Description
> This [garden](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg) contains more than it seems.
>
> **Hint 1: Finding a cheatsheet for bash would be really helpful!**

### Solution
The link provided downloads an image of a garden. Right off the bat we can run `strings` on the image to see if there are any obvious static strings embedded within the image. Surprisingly, this worked.

### Flag
`picoCTF{more_than_m33ts_the_3y33dd2eEF5}`
