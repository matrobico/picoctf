# Corrupted File
> Forensics

### Description
> This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life?
> 
> You can download the challenge files [here](https://artifacts.picoctf.net/c_rhea/20/challenge.zip):

### Solution
The file is a corrupted file. Based on the challenge description, it's probable that this file is a couple bytes off of its file format.

Grabbing the file and taking a look, it appears to be a JPG image file. Comparing to the file format for this media type, we can see the first 2 bytes are incorrect. Changing them to the proper beginning 2 bytes for JPG files (FF D8), and then adding the ".jpg" file extension, we can open the image and view the flag.

### Flag
`picoCTF{r3st0r1ng_th3_by73s_efd8c6c0}`
