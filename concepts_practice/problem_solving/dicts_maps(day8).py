n = int(input())
phone_book = {}

for i in range(n):
    listy = list(map(str, input().split()))
    key = listy[0]
    value = listy[1]
    phone_book[key] = value

while True:
    try:
        name = input()
        if name in phone_book:
            print(name + " = " + phone_book[name])
        else:
            print("Not found")
    except:
        break


