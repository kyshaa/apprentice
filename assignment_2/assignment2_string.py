# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:53:23 2021

@author: Alkisah Mubin

Assignment 2 (a) : String Methods and Functions
"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Capitalized first letter of string
#    Method : capitalize()

str1 = """this is string example....wow!!!"""
print (str1.capitalize())


# 1.1 Practice capitalize first letter each after punctuation

str2 = """guten tag. ich bin Alkisah.sehr angenehm.wie geht's'"""

list = str2.split(".")                                              # split/divides str into a list means divides word until period mark

if str2.endswith('.'):
    list.remove('')

for w in list:
    stripper= w.strip().capitalize() +"."                           # strip removes characters from the start and/or end of a string
    print(stripper, end=" ")
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 2. Returns a space-padded string with the original string centered to a total of width columns
#    Method : center(width, fillchar)

str1 = "this is string example....wow!!!"
print (str1.center(40, 'a'))

# 2.1 Practice left pad a string with some character using string.rjust()
print (str1.rjust(40, 'a'))

# 2.2 Practice left pad a string with zeros using string.zfill()
print (str1.zfill(40))

# 2.3 Practice left pad a string with space using string.rjust() -> string.rjust(s, width[, fillchar])
print (str1.rjust(40, ' '))

# 2.4 Practice right pad a string with some character using string.ljust() -> string.ljust(s, width[, fillchar])
print (str1.ljust(40, 'a'))

# 2.5 Practice right pad a string with zeros using string.ljust() -> string.ljust(s, width[, fillchar])
print (str1.ljust(40, '0'))

# 2.6 Practice right pad a string with space using string.ljust()
print (str1.ljust(40, ' '))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. Counts how many times str occurs in string or in a substring of string if starting index "beg" and ending index "end" are given.
#    Method : count(str, beg= 0,end=len(string))

#    sub − This is the substring to be searched
#    start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index
#    end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.

str1 = "this is string example....wow!!!"
sub = "i"

print ("str1.count(sub, 4, 40) : ", str1.count(sub, 4, 40))

sub = "wow";
print ("str1.count(sub) : ",
str1.count(sub))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 4. Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.
#    Method : bytes.decode(encoding="utf-8", errors="strict")

city = "Düsseldorf"
utf8_encoded = city.encode('utf-8')

print(type(utf8_encoded))                               # bytes
print(utf8_encoded)                                     # b'D\xc3\xbcsseldorf'

decoded_city = utf8_encoded.decode('utf-8')

print(type(decoded_city))                               # str
print(decoded_city)                                     # Düsseldorf


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 5. Return a string decoded from the given bytes. Default encoding is 'utf-8'. errors may be given to set a different error handling 
#    scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError.
#    Method : str.encode(encoding="utf-8", errors="strict")


city = "Düsseldorf"
utf8_encoded = city.encode('utf-8')

print(type(utf8_encoded)) # bytes
print(utf8_encoded) # b'D\xc3\xbcsseldorf'

decoded_city = utf8_encoded.decode('utf-8')

print(type(decoded_city)) # str
print(decoded_city) # Düsseldorf


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 6. Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
#    Method : endswith(suffix, beg=0, end=len(string))

str1 = "this is string example....wow!!!"
suffix = "wow!!!"

print (str1.endswith(suffix))
print (str1.endswith(suffix,20))

suffix = "is"
print (str1.endswith(suffix, 2, 4))
print (str1.endswith(suffix, 2, 6))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 7. Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided. 
#    Method : expandtabs(tabsize=8)

 
str1 = "this is\tstring example....wow!!!"
print ("Original string: " + str1)
print ("Default exapanded tab: " + str1.expandtabs())
print ("Double exapanded tab: " + str1.expandtabs(16))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 8. Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
#    Method : find(str, beg=0 end=len(string))

str1 = "this is string example....wow!!!"
str2 = "exam"
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 9. Same as find(), but raises an exception if str not found.
#    Method : index(str, beg=0, end=len(string))

str1 = "this is string example....wow!!!"
str2 = "exam"
print (str1.index(str2))
print (str1.index(str2, 10))
print (str1.index(str2, 40))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 10. Returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
#     Method : isalnum()

str1 = "this2009";                                       # No space in this string
print (str1.isalnum())

str1 = "this is string example....wow!!!"
print (str1.isalnum())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 11. True  - If all characters in the string are alphabet.
#     False - If the string contains 1 or more nonalphabets.
#     Method : isalpha()

str1 = "this2009";                                        # No space in this string
print (str1.isalpha())

str2 = "this is string example....wow!!!"
print (str2.isalpha())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 12. Returns true if string contains only digits and false otherwise.
#     Method : sdigit()

str1 = "123456"                                           # Only digit in this string
print (str1.isdigit())

str2 = "this is string example....wow!!!"
print (str2.isdigit())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 13. Returns True if string has at least 1 cased  character and all cased characters are in lowercase and false otherwise.
#     Method : islower()
 
str1 = "THIS is string example....wow!!!"
print (str1.islower())

str2 = "this is string example....wow!!!"
print (str2.islower())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 14. Returns True if a unicode string contains only numeric characters and False otherwise
#     Method : isnumeric()

str1 = u"this2009" 
print (str1.isnumeric())

str2 = u"23443434"
print (str2.isnumeric())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 15. Returns True if string contains only whitespace characters and False otherwise
#     Method : isspace()

str1 = " "
print (str1.isspace())

str2 = "This is string example....wow!!!"
print (str2.isspace())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 16. Returns True if string is properly "titlecased" and False otherwise
#     Method : istitle()

str1 = "This Is String Example...Wow!!!"
print (str1.istitle())

str2 = "This is string example....wow!!!"
print (str2.istitle())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 17. Returns True if all characters in a string are uppercase characters and False otherwise 
#     Method : isupper()

str1 = "THIS IS STRING EXAMPLE....WOW!!!"
print (str1.isupper())

str2 = "THIS is string example....wow!!!"
print (str2.isupper())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 18. Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string
#     Method : join(seq)

s = "-"
seq = ("a", "b", "c");                                      # This is sequence of strings.
print (s.join( seq ))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 19. Returns the length of the string
#     Method : en(string)

str1 = "this is string example....wow!!!"
print ("Length of the string: ",
len(str1))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 20. Returns a space-padded string with the original string left-justified to a total of width columns.
#     Method : ljust(width[, fillchar])

str1 = "this is string example....wow!!!"
print (str1.ljust(50, '0'))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 21. Converts all uppercase letters in string to lowercase
#     Method : lower()

str1 = "THIS IS STRING EXAMPLE....WOW!!!"
print (str1.lower())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 22. Removes all leading whitespace in string or returns a copy of the string in which all chars have been stripped from the beginning of the string
#     Method : lstrip()

str1 = " this is string example....wow!!! "
print (str1.lstrip())

str2 = "88888888this is string example....wow!!!8888888"
print (str2.lstrip('8'))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 23. Returns a translation table to be used in translate function. 
#     Method : maketrans()

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str1 = "this is string example....wow!!!"
print (str1.translate(trantab))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 24. Returns the max alphabetical character from the string str.
#     Method : max(str)

str1 = "this is really a string example....wow!!!"
print ("Max character: " + max(str1))

str2 = "this is a string example....wow!!!"
print ("Max character: " + max(str2))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 25. Returns the min alphabetical character from the string str
#     Method : min(str)

str1 = "this-is-real-string-example....wow!!!"
print ("Min character: " + min(str1))

str2 = "this-is-a-string-example....wow!!!"
print ("Min character: " + min(str2))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 26. Replaces all occurrences of old in string with new or at most max occurrences if max given 
#     Method : replace(old, new [, max])

str1 = "this is string example....wow!!! this is really string"
print (str1.replace("is", "was"))
print (str1.replace("is", "was", 3))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 27. Same as find(), but search backwards in string 
#     Method : rfind(str, beg=0,end=len(string))

str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 28. Same as index(), but search backwards in string
#     Method : rindex( str, beg=0, end=len(string))

str1 = "this is string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.index(str2))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 29. Returns the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). 
#     The original string is returned if width is less than len(s).
#     Method : rjust(width,[, fillchar])

str1 = "this is string example....wow!!!"
print (str1.rjust(50, '0'))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 30. Returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters).
#     Method : rstrip()

str1 = " this is string example....wow!!! "
print (str1.rstrip())
str2 = "88888888this is string example....wow!!!8888888";
print (str2.rstrip('8'))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 31. Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given
#     Method : split(str="", num=string.count(str))

str1 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print (str1.split( ))
print (str1.split(' ', 1 ))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 32. Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed
#     Method : splitlines( num=string.count('\n'))

str1 = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d"
print (str1.splitlines( ))
print (str1.splitlines( 0 ))
print (str1.splitlines( 3 ))
print (str1.splitlines( 4 ))
print (str1.splitlines( 5 ))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 33. Determines if string or a substring of string (if starting index beg and ending index end 
#     are given) starts with substring str; returns true if so and false otherwise
#     Method : startswith(str, beg=0,end=len(string))

str1 = "this is string example....wow!!!"
print (str1.startswith( 'this' ))
print (str1.startswith( 'is', 2, 4 ))
print (str1.startswith( 'this', 2, 4 ))
       
       
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 34. Performs both lstrip() and rstrip() on string
#     Method : strip([chars])

str1 = "0000000this is string example....wow!!!0000000"
print (str1.strip( '0' ))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 35. Inverts case for all letters in string
#     Method : swapcase()

str1 = "this is string example....wow!!!"
print (str1.swapcase())

str1 = "THIS IS STRING EXAMPLE....WOW!!!"
print (str1.swapcase())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 36. Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase
#     Method : title()

str1 = "this is string example....wow!!!"
print (str1.title())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 37. Translates string according to translation table str(256 chars), removing those in the del string
#     Method : translate(table, deletechars="")

intab = "aeiou"
outtab = "12345"
str1 = "this is string example....wow!!!"
trantab = str.maketrans(intab, outtab)
print (str1.translate(trantab))

# 37.1 Practice example to delete 'x' and 'm' characters from string

trantab = str.maketrans(intab, outtab, 'xm')
print (str2.translate(trantab))



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 38. Converts lowercase letters in string to uppercase
#     Method : upper()

str1 = "this is string example....wow!!!"
print ("str1.capitalize() : ",
str1.upper())


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 39. Returns original string leftpadded with zeros to a total of width characters; intended for numbers, 
#     zfill() retains any sign given (less one zero).
#     Method : zfill (width)

str1 = "this is string example....wow!!!"
print (str1.zfill(40))
print (str1.zfill(50))


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 40. Returns true if a unicode string contains only decimal characters and false otherwise 
#     Method : isdecimal()

str1 = u"this2009" 
print (str1.isdecimal())

str2 = u"23443434"
print (str2.isdecimal())

