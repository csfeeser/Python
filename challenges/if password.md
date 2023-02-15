## If-Logic Practice

<img src="https://images3.memedroid.com/images/UPLOADED93/62c4023490bf9.jpeg" width="200"/>

**Objective:** finish the code below. The user will type in a prospective password, saving it as the variable `passwoid`. Write a program that will check if:
- the password a minimum of 8 characters in length?
- the password starts with a capital "P" (`p` for Python!)
- the password ends with 3 (like `Alta3`!)
- the password does NOT have the word "butts" in it (there's a lot of immature people at this company)
- announce whenever one of these tests fails.

```python
import getpass

# the getpass function from the getpass module is 
# like a "private" version of input()

passwoid= getpass.getpass()

# SUGGESTED FUNCTIONS/METHODS
# len() <-- counts the number of iterables in an object
# str.endswith() <-- checks if a string starts with a character
# str.startswith() <-- checks if a string ends with a character

# is the password a minimum of 8 characters in length?

# does the password start with a capital "P"?

# does the password end with 3?

# does the password NOT have the word "butts" in it?
```
