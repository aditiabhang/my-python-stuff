import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search("My number is 213-321-2132")
print(mo.group())
print("Area code:", mo.group(1))