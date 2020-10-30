#Replaces Flight with Plane
#To replace the word "Flight" with the word "Plane".
import re
flight_details="Flight Savana Airlines a2134"
print(re.sub(r"Flight",r"Plane",flight_details))

#() is used to group characters. Here we are grouping 4 numbers together and referring it as \1. 1 indicates the first group
#To replace the ‘a’ to ‘A’ if it is followed by 4 numbers.
import re
flight_details="Flight Savana Airlines a2134"
print(re.sub(r"a(\d{4})",r"A\1",flight_details))
