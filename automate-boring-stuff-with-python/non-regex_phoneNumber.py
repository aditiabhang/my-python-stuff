def isPhoneNumber(text): #713-369-3699
    if len(text) != 12:
        return False    # not phone number-sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False    # no area code
    if text[3] != '-':
        return False    # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False    # no first 3 digits
    if text[7] != '-':
        return False    # second dash missing
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


# print("Please enter your phone number:")    
# phone = input()
# print(isPhoneNumber(phone))

message = "Call me on 713-369-3699 tomorrow or 713-369-3669 for the office line."
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
        foundNumber = True

if not foundNumber:
    print("Could not found any phone numbers.")
