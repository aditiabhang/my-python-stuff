import statistics

A = ['+1A', '-1A', '+3F', '-3F', '+3F','+8X']


res = statistics.mode(A)
print("Most often : ", str(res[1:]))