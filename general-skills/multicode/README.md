# MultiCode
> General Skills

### Description
> We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?
>
> Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/5119ccb146ea34b59ef1a4a360d994422181bf88b136079fc09df33bdf091fdf/message.txt).
>
> **Hint 1**: The flag has been wrapped in several layers of common encodings such as ROT13, URL encoding, Hex, and Base64. Can you figure out the order to peel them back?
>
> **Hint 2**: A tool like CyberChef can be interesting.

### Solution
Throw the flag into CyberChef and use the following recipe:

- From Base64
- From Hex
- ROT13
- URL Decode


### Flag
`picoCTF{nested_enc0ding_ffbbbf57}`
