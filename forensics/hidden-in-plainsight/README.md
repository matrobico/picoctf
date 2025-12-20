# Hidden in Plainsight
> Forensics

### Description
> You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

### Solution
Using exiftool to view metadata for ideas, we can see the comment field contains a base64 string (steghide:cEF6endvcmQ=) that when decoded, says "steghide:pAzzword".

Googling "steghide", it's an online tool. It seems we have to use steghide to extract the enctypted message it stored within this file, then decrypt it with the given password (pAzzword).

### Flag
TO ADD (steghide download not working right now)
