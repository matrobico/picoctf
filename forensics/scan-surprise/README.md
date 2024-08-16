# Scan Surprise
> Forensics

### Description
> I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead?
>
> You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_atlas/1/challenge.zip)
> 
> Additional details will be available after launching your challenge instance.
>
> **Hint 1: QR codes are a way of encoding data. While they're most known for storing URLs, they can store other things too**
>
> **Hint 2: Mobile phones have included native QR code scanners in their cameras since version 8 (Oreo) and iOS 11**
>
> **Hint 3: If you don't have access to a phone, you can also use zbar-tools to convert an image to text**

### Solution
We're presented with a QR code. Simply parsing the image using a phone reveals the flag.

### Flag
`picoCTF{p33k_@_b00_3f7cf1ae}`
