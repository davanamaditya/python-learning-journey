name = "Aditya"
print("Hello " + name)
print(name.upper())
print(name.lower())
print(len(name))
name = "Aditya"
print(type(name))
age = 24
newage = age + 5
print(type(age))
print("your age is:" + str(newage))
#str is needed to prit int along with string
#maths
#len() it is used to cout no of items in a value
password = "123a"
print(len(password))
if len(password) < 8:
    print("your password is too short")
#count is used to count the no of occurences of a character in a string
print(password.count("p"))
#replace is used to replace a character in a string with another character
print(password.replace("1", "2"))
#challenge
phone_number = "+49 (123) 456-7890"
# Remove the country code and any non-digit characters
phone_number = phone_number.replace("+49", "49").replace("(123)", "123").replace("-", "").replace(" ", "")
print(phone_number)
 #f-strings are used to format strings in a more readable way
name = "Aditya"
age = 24
print(f"My name is {name} and I am {age} years old.")       
print(f"2+45 = {2+45}")
#split() is used to split a string into a list of substrings based on a delimiter
sentence = 'This is a sample sentence.'
words = sentence.split(" ")
print(words)
#transforming a string into a list of characters
string = "Hello"
char_list = list(string)
print(char_list)    
print("ha" *34)
#extracting a substring from a string
string = "Hello, World!"
substring = string[7:12]#7 is the start and 12 is the end index, it will extract the characters from index 7 to 11
print(substring)
print(string[0])
#white space is used to remove the white space from the beginning and end of a string
string = "  Engeering"
print(len(string))
print(len(string.strip()))
no_of_spaces = len(string) - len(string.strip())
print("no of spaces in the string is: " + str(no_of_spaces))

