# Printer Shares
> General Skills

### Description
> Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?
>
> **Hint 1**:

### Solution
On a Mac, `smbclient` can be used to interact with an smb server.

```
smbclient //mysterious-sea.picoctf.net/shares -p 59215 -N
get flag.txt
```
### Flag
`picoCTF{5mb_pr1nter_5h4re5_7a400ec3}`
