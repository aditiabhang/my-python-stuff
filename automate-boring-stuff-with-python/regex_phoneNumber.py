import re

message = "Call me on 713-369-3699 tomorrow or 713-369-3669 for the office line."

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumberRegex.findall(message) # search() - returns first occurance
print(matchObject)

# findall() - returns LIST of matches found. Hence, need to print it. 
# search() - returns single output. 