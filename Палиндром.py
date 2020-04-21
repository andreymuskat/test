world_or_number = input()
string = str(world_or_number)
rev_string = string[::-1]
if string == rev_string:
    print("palindrome")
else:
    print("not palindrome")
