# Flag in Flame
> Forensics

### Description
> The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
>
> Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

### Solution
The file given is a giant single line of text containing encrypted data. If we cat this data out, we can see it's base64 encoded. Decoding this data and piping out to a new file, we can see it's a PNG image file. Opening this file, we see a hex string (all hex characters - 0-9 and A-F values), which we decoded, gives us the flag.

### Flag
`picoCTF{forensics_analysis_is_amazing_2561a194}`
