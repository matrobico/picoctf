# Hackcrack
> Cryptography

### Description
> A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

### Solution
Upon starting the challenge instance and netcatting to the server, we're given a hash and told to enter the password for the hash. We should be able to just use hashcat over this hash to crack our pasword and get in. Since the given hash is 33 characters long, it's likely it's an MD5 hash that's been salted in some way. Using hashcat on this, we get another hash (SHA1), then another (SHA256) - both of which we know the hash type based on length, until we get our flag.

```
hashcat -a 0 -m 0 482c811da5d5b4bc6d497ffa98491e38 /usr/share/wordlists/rockyou.txt
-> password123

hashcat -a 100 -m 0 b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3 /usr/share/wordlists/rockyou.txt
-> letmein

hashcat -a 1400 -m 0 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745 /usr/share/wordlists/rockyou.txt
-> picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4de57566}
```


### Flag
`picoCTF{UseStr0nG_h@shEs_&PaSswDs!_4de57566}`
