"""
Author: Muhammad Ahsan Adnan
Verison: 1.0
Description: Script that interacts with the Ontology Lookup Service and uses theri API to get 
the data and display it to the user.
"""

#Taking the user Ontology ID as input and converting it to lowercase to avoid case sensitivity
print("Welcome to the Ontology Lookup Service!")
input = input("Please enter the Ontology ID: ")
input = input.lower()
print("You entered: " + input)