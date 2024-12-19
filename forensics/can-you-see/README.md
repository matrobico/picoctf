# CanYouSee
> Forensics

### Description
> How about some hide and seek?
>
> Download this file [here](https://artifacts.picoctf.net/c_titan/128/unknown.zip).
>
> **Hint 1**: How can you view the information about the picture?
>
> **Hint 2**: If something isn't in the expected form, maybe it deserves attention?

### Solution
Opening up the file is benign enough, as it's just an image. Opening up the file as text shows references to "XMP", meaning there's probably embedded metadata within this image. Using exiftool, we can see an odd base64 looking string for "Attribution URL". Decoding this string reveals the flag.

### Flag
`picoCTF{ME74D47A_HIDD3N_3b9209a2}`
