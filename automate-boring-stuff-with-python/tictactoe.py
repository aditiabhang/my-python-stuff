# this code is just a display of dictionary data structure

theBoard = {'top-L': 'O ', 'top-M': 'O ', 'top-R': 'O ',
            'mid-L': '  ', 'mid-R': 'X ', 'mid-M': '  ',
            'low-L': '  ', 'low-R': '  ', 'low-M': 'X '}

'''>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
'''

# printing the board
def printBoard(board):
    print('| ' + board['top-L'] + '| ' + board['top-M'] + '| ' + board['top-R'] + '|')
    print('-------------')
    print('| ' + board['mid-L'] + '| ' + board['mid-M'] + '| ' + board['mid-R'] + '|')
    print('-------------')
    print('| ' + board['low-L'] + '| ' + board['low-M'] + '| ' + board['low-R'] + '|')
    print('-------------')

printBoard(theBoard)