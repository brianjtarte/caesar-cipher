# LAB - Class 18 
## Project: Caesar Cipher
### Author: Brian T.
### Collaborators: Brendon H.

## Feature Tasks and Requirements
1. Create an encrypt function that takes in a plain text phrase and a numeric shift.
   1. the phrase will then be shifted that many letters.
        1. E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.
   2. shifts that exceed 26 should wrap around.
      1. E.g. encrypt(‘abc’,27) would return ‘bcd’.
2. shifts that push a letter out or range should wrap around.
3. E.g. encrypt(‘zzz’,1) would return ‘aaa’. 
4. Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied. 
5. create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key. 
6. Devise a method for the computer to determine if code was broken with minimal human guidance.

### Links and Resources

### Setup
`.env` requirements (where applicable)

**i.e.**

- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db
#### How to initialize/run your application (where applicable)
*python caesar_cipher/caesar_cipher.py*
#### How to use your library (where applicable)
#### Tests
- How do you run tests?
*pytest test_caeser.py*
- Any tests of note?
- Describe any tests that you did not complete, skipped, etc