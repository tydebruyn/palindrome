def reverse(string):
    reverse_string = []

    #loop through string
    for i in range(1, len(string) + 1):
        #last didget of string -> first didget of reverse_string
        reverse_string.append(string[-i])

    #change array into string
    return "".join(reverse_string)

normal_string = "racecar"
reverse_string = reverse(normal_string)

#check if palindrome
if normal_string == reverse_string:
    print reverse_string
    print "palindrome."
else:
    print normal_string
    print reverse_string
    print "not a palindrome."
