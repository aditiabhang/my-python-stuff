import pprint

message = 'Today is the 11 May of Summer 2020 and the clock right now is stricking 1'
count = {}

romeoandjuliet = '''can insert 100000s of works'''

for character in message: # message.upper() - to make it all upper case
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)