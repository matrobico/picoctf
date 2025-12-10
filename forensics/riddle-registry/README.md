# Riddle Registry
> Forensics

### Description
> Hi, intrepid investigator! You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.

Find the PDF file here and uncover the flag within the metadata.

### Solution
The flag is contained within the metadata of the PDF. File metadata is just data about the file (e.g., author, creation date, etc) that is stored in the file format. So we can use a tool for viewing metadata contained in media files, like exiftool.

Using exiftool, we can see the author field contains base64 text, which when decoded, reveals the flag.

### Flag
`picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}`
