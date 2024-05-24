# Speeds and Feeds
> Reverse Engineering

### Description
> There is something on my shop network running at nc mercury.picoctf.net 59953, but I can't tell what it is. Can you?
>
> **Hint 1: What language does a CNC machine use?**
>

### Solution
Using netcat to the given link, we're met with a display of much of the following:

```
G1X25.6552Y0.8276
G1X25.9310Y1.3793
G0Z0.1
G0X23.7241Y5.7931
G1Z0.1
...
```

Googling `G0Z0.1` (since that seems to be repeated and could be a "key" piece of information), it seems this is part of a programming language called "G-code" for "CNC machines".

Knowing that, we can look up the programming language and its mechanics to decipher this code. Better yet, we can output the netcat results to a file and feed that file into an G-code interpeter (e.g., like [this](https://ncviewer.com) one.


### Flag
`picoCTF{num3r1cal_c0ntr0l_f3fea95b}`
