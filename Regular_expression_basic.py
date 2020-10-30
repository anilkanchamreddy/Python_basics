#Checks if pattern “Air” is found in “Airline”
#r"Air" here r in front indicates the raw data

import re
if(re.search(r"Air","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
    
#“.” stands for any character. If any two characters are there between A and l, then the pattern has matched
import re
if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#\d checks for a digit. If any digit is found between A and l, then pattern is found
import re
if(re.search(r"A\dl","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#[] does a single character substitution. We can specify a sequence of values. If any of the values are found, then the pattern has matched
import re
if(re.search(r"A[4-8]l","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# | acts like ‘or’ operator. If Hell or Fell is found in the string, the pattern is found
import re
if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#\s indicates a space. Here we are checking if there is a space after Air
import re
if(re.search(r"Air\s","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#Checks if a number is found 0 or n times after A
#To check if a number is found 0 or n times after A in the given string.
import re
if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#Checks if a number is found 1 or n times after A
#To check if a number is found 1 or n times after A in the given string.
import re
if(re.search(r"A\d+","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#Checks if a number is found 0 or 1 times after A
#To check if a number is found 0 or 1 times after A in the given string.
import re
if(re.search(r"A\d?i","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
#{n} checks if the preceding character appears exactly n times. Here we are checking if there are 3 digits after A
#To check if 3 digits are present after A in the given string.
import re
if(re.search(r"A\d{3}i","A223irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# ^ checks if a pattern is at the beginning of the string. Here we check if string begins with “A”
#To check if the given string is starting with A.
import re
if(re.search(r"^A","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# $ checks if a pattern is at the end of the string. Here we check if string ends with “e”
#To check if the given string is ending with e
import re
if(re.search(r"e$","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

#\w checks for a-z,A-Z,0-9,_ Here we check if the last character is an alphanumeric character
#To check whether last character is alphanumeric or not.
import re
if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# \ is used to escape special characters
# To escape a special character
import re
if(re.search(r"\*","Air*line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
