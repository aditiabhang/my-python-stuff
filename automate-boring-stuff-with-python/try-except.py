def div42ByNum(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: try to divide by zero!")

print(div42ByNum(2))
print(div42ByNum(12))
print(div42ByNum(6))
print(div42ByNum(0))
print(div42ByNum(24))

# A divide-by-zero error happens when Python divides a number by zero.
# Errors cause the program to crash. (This doesn't damage your computer at all. 
# It's just that the computer doesn't know how to carry out this instruction, 
# so it immediately stops the program by "crashing" rather than continue.)
# An error that happens inside a try block will cause code in the except block to execute. 
# That code can handle the error or display a message to the user so that the program can keep going.