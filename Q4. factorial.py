#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/submissions/


def factorial():
    Fact = 1
    N = int(input())
    for _ in range(1,N+1):
        Fact *= _
    return Fact
print(factorial())