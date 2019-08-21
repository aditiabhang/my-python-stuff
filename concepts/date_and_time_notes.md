- The datetime Library
A lot of times you want to keep track of when something happened. We can do so in Python using datetime.
Here we’ll use datetime to print the date and time in a nice format.

=> from datetime import datetime

- We can use a function called datetime.now() to retrieve the current date and time.

from datetime import datetime
print datetime.now()

The first line imports the datetime library so that we can use it.
The second line will print out the current date and time.

- Example:
from datetime import datetime
now = datetime.now()
print now

Also,
print now.year
print now.month
print now.day
----------------------------------------------------------------------
- Hot Date
What if we want to print today’s date in the following format? mm/dd/yyyy. Let’s use string substitution again!

from datetime import datetime
now = datetime.now()

print '%02d-%02d-%04d' % (now.month, now.day, now.year)
# will print the current date as mm-dd-yyyy.
# %02d pads the month and day numbers with zeros to two places, and %04d pads the year to four places.
Similary for time:
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)
----------------------------------------------------------------------
