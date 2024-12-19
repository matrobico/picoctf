# Secret of the Polyglot
> Forensics

### Description
> The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file?

> Download the suspicious file [here](https://artifacts.picoctf.net/c_titan/99/flag2of2-final.pdf).

>
> **Hint 1: This problem can be solved by just opening the file in different ways.**

### Solution
Runnings strings on the file displays a flag (`picoCTF{qu1t3_a_v13w_2020}`), but this is apparently a red herring.

Running the `file` command shows that this is indeed interpreted as a PNG file, and opening it in any image viewing application displays the first part of the flag:

`picoCTF{f1u3n7_`

From running strings on this file earlier, we can see references to "ghostscript", "pdf", and other metadata that might indicate this file is also a valid PDF file. However, changing the extension to `.pdf` and trying to open it isn't working on my Mac. Therefore, we can try using the ghostscript command line tool (since we see a reference to it) to parse out this image. Or alternatively, we can use `pdftotext` to print out the PDF text in this file. Either reveals the second part of the flag:

`1n_pn9_&_pdf_2a6a1ea8}`

### Flag
`picoCTF{f1u3n7_1n_pn9_&_pdf_2a6a1ea8}`
