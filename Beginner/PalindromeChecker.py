def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]
while True:
    # Test the function
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("Yes, it's a palindrome!")
    else:
        print("No, it's not a palindrome.")