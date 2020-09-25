# Q2.https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

word  = input().lower()
x = 0
y = 0

for i in range(len(word)):
    if word[i] == "z":
        x  += 1
    elif word[i] == "o":
        y += 1
    else:
        break

if 2*x == y and x!=0:
    print("Yes")
else:
    print("No")