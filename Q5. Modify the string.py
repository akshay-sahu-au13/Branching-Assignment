# Q5.https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/


def toggle_str():

    Str = input()
    Rev = ""
    for i in Str:

        if i.isupper():
            Rev += i.lower()
        else:
            Rev += i.upper()
    return print(Rev)

toggle_str()