def checkpalindrome(string):
    string = string.lower()
    if string == string[::-1]:
        print("String is a palindrome")
        return True
    else:
        print("String is not a palindrome")
        return False
    
if __name__ == "__main__":
    string = input("Enter string: ")
    checkpalindrome(string)