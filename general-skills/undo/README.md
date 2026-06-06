# Verify
> General Skills

### Description
> Can you reverse a series of Linux text transformations to recover the original flag?

**Hint**: For text translation and character replacement, see tr command documentation.

### Solution
- 1) `base64 -d`
- 2) `rev`
- 3) `tr '()' '{}'`
- 4) `tr 'A-Za-z' 'N-ZA-Mn-za-m'`

### Flag
`picoCTF{qu1t3_a_v13w_2020}`
