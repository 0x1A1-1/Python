def palindrome(str):
    for i in range(0, (len(str)-1)/2):
        if str[i]!=str[len(str)-1-i]:
            return False
    return True

def palindromeTest():
    for i in ["hih", "racecar", "stuff"]:
        print palindrome(i)

def reverse(str):
    return str[::-1]

palindromeTest()
