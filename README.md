# PyPwGen
A fast python password generator that creates intuitive, secure passwords.

PyPwGen is a simple program which generates a password using words instead of just characters and numbers. Using words allow our password to be remembered easily, while keeping them as secure if not more secure than traditional alphanumeric passwords.

### How it works
PyPwGen fetches three random words from a text file and combines them together along with a 3-digit number to create a password. Using [combinatorics](https://en.wikipedia.org/wiki/Combinatorics), we can easily calculate the number of unique passwords this program can generate:

```
Number of words in text file: 2926
We have 3 words per password, followed by a 3-digit number (000 to 999)

2926 * 2926 * 2926 * 999 = 25,025,827,897,224 possible passwords.
```
This number can be drastically improved by simply adding a few more words to the text file. 

## Future improvements:
- Instead of pulling 3 words from one file, have three different files, each containing adjectives, nouns, and verbs respectively. This would make passwords even easier to remember while also greatly increasing the number of unique passwords the program can generate.
- Generation configuration (4 or 5-digit numbers instead of 3, 4 words, etc.)
