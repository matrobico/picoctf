# Shop
> Reverse Engineering

### Description
> Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/a94b408ab46e6bd72f915d68be8aebc0/source). The shop is open for business at nc mercury.picoctf.net 42159.
>
> **Hint 1: Always check edge cases when programming**
>

### Solution
We're given a binary and a netcat link to a running instance of said binary. This challenge can be solved by simply interacting with program and exloring its bounds.

We're initially met with a welcome message and a shop. We can see our available options are to buy or sell several items and we're given an initial currency. If we stay within our currency limits, there's no problem buying or selling anything. However, if we get a little creative and try using negative numbers when purchasing an item, we can see some interesting behavior - our currency goes up! It seems there's no sanitization going on, and so our negative value gets subtracted from our currency, resulting in an increase. Knowing that, we can give ourselves as much money as we want to purchase the "Fruitful Flag".

Purchasing that yields:
'''
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 55 57 55 98 50 57 50 99 125]
'''

Which is clearly ASCII, so we can decode that to arrive at our flag.

### Flag
`picoCTF{b4d_brogrammer_797b292c}`
