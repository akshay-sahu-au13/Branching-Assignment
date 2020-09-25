# Q3.https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

def is_pallindrome():

    Str = input()
    if Str == Str[::-1]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":

    print(is_pallindrome())