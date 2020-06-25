### Q.1. arithmaticShift :
- Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase English characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 1000.

[output] string

The resulting string after replacing each of its characters.

### Q.2. tailTheFile :
- The tail command is a core utility which can be used to look at the end of a text file. It's primarily used for reading and analyzing log files as they're being written, which is especially useful for monitoring the logging process.

Your task is to implement a basic tail utility, which will return last n lines of a given log file. The utility should read from the /root/devops/logs/tail.conf configuration file to get the value of n, then parse the log file located in /root/devops/logs/file.log, and print the last n lines of file.log to the stdout.

It's guaranteed that config file will contain only one number - n.

### Q.3. buildPalindrome :
- Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string

### Q.4. countBinarySequence :
- Given integers n and k, find the number of the sequences of length n consisting of only 0s and 1s in which there are no consecutive k 1s.

Example

For n = 3 and k = 2, the output should be
countBinarySequences(n, k) = 5.
Here are they:

000
001
010
100
101
other 3 sequences - 011, 110 and 111 have 2 consecutive 1s, so they don't satisfy the condition.