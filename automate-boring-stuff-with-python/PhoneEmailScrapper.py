#! python 3

import re, pyperclip

# 1. Create regex object for phone numbers

# phoneRegex = re.compile(r'''
# # 555-333-0000, 333-6666, (333) 444-2222, 333-6666 ext 12354, ext. 12345, x12345
# (      
# ((\d\d\d) | (\(\d\d\d\))?   # area-code (optional)
# (\s|-)                      # fist separator
# \d\d\d                      # first 3 digits
# -                           # second dash
# \d\d\d\d                    # last 4 digits
# (((ext(\.)?\s)| x)          # extension word-part (optional)
# (\d{2,5}))?                 # extension number-part (optional)
# )
# ''', re.VERBOSE)
#--------------------------------------------------
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# 2. Create regex object for email addresses

# emailRegex = re.compile(r'''

# #some.+_thing@(\d{2,5})?.com

# [a-zA-Z0-9_.+]+              # name part
# @                           # @ symbol
# [a-zA-Z0-9_.+]+              # domain part

#  ''', re.VERBOSE)
#----------------------------------------------
emailRegex = re.compile(r'''(
     [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
     [a-zA-Z0-9.-]+         # domain name
     (\.[a-zA-Z]{2,4})      # dot-something
     )''', re.VERBOSE)


# 3. Get the text off the clipboard
text = pyperclip.paste()

# 4. Extract email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# 5. Copy extracted email/phone on the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

