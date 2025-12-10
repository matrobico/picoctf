# Log Hunt
> Forensics

### Description
> Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?
>
> Download the logs and figure out the full flag from the fragments.

### Solution
The flag is contained in split pieces within the log file. It seems to outputted with each "INFO FLAGPART" log line. So we can just grep for these instances and put the pieces together.

### Flag
`picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}`
