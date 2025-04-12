# string is a sequence of characters
# strings are "immutable" which means they cannot be changed after they are created

name = 'Sakib\'s khan' #escape single quote
name2 = "Sakib\"s khan" #escape double quote
name3 = "Sakib khan" #raw string

#multiline string with triple quotes
name4 = """
Sakib khan
Sakib khan2
"""

print(name)
print(name2)
print(name3)
print(name4)

#basic string operations
print(name[0]) #first character


print(name[1:5]) #slice from index 1 to 4
print(name[1:]) #slice from index 1 to end
print(name[:5]) #slice from start to index 4
print(name[-1]) #last character

print(name[-2]) #second last character  
print(name[-2:]) #slice from second last to end
print(name[:-2]) #slice from start to second last
print(name[-2:-1]) #slice from second last to last

#string length
print(len(name)) #length of string
print(len(name4)) #length of multiline string

#string concatenation
name5 = name + " " + name2 #concatenate two strings
print(name5) #print concatenated string

#string multiplication
name6 = name * 3 #multiply string
print(name6) #print multiplied string

#string methods
print(name.lower()) #convert to lowercase
print(name.upper()) #convert to uppercase
print(name.title()) #convert to titlecase
print(name.capitalize()) #convert to capitalized case
print(name.strip()) #remove whitespace from start and end
print(name.lstrip()) #remove whitespace from start  
print(name.rstrip()) #remove whitespace from end
print(name.replace("Sakib", "Sakib")) #replace string
print(name.split(" ")) #split string into list
print(name.split("k")) #split string into list
print(name.splitlines()) #split string into list of lines
print(name.find("Sakib")) #find substring in string
print(name.index("Sakib")) #find substring in string
print(name.count("Sakib")) #count substring in string
print(name.startswith("Sakib")) #check if string starts with substring
print(name.endswith("khan")) #check if string ends with substring
print(name.isalnum()) #check if string is alphanumeric
print(name.isalpha()) #check if string is alphabetic    
print(name.isdigit()) #check if string is digit
print(name.isnumeric()) #check if string is numeric
print(name.isdecimal()) #check if string is decimal
print(name.isidentifier()) #check if string is identifier
print(name.islower()) #check if string is lowercase
print(name.isupper()) #check if string is uppercase
print(name.istitle()) #check if string is titlecase