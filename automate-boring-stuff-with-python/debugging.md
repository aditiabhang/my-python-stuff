### The raise and assert statements:
- You can raise your own exceptions: raise Exception(**‘This is the error message.'**)
- You can also use assertions: assert condition, ‘Error message'
- Assertions are for detecting programmer errors that are not meant to be recovered from. User errors should raise exceptions.