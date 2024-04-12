"""
Author: Muhammad Ahsan Adnan
Verison: 1.0
Description: Script that interacts with the Ontology Lookup Service and uses their API to get 
the data and display it to the user.
"""
import json
import requests

#Taking the user Ontology ID as input and converting it to lowercase to avoid case sensitivity
print("Welcome to the Ontology Lookup Service!")
while True:
    id_input = input("Please enter the Ontology ID (or press 'q' to quit): ")
    id_input = id_input.lower()
    #Allow the user to quit the program
    if id_input == "q":
        print("Thank you for using the Ontology Lookup Service!")
        break

    #Function to get the ontology details so that it can be reused as a library function
    def get_ontology_details(id_input):
        #Using the API to get the data from the Ontology Lookup Service
        url = "https://www.ebi.ac.uk/ols4/api/ontologies/" + id_input
        response = requests.get(url)
        #Incase the id doesnt exist it returns an error so we check for that and ask the user to enter a valid id
        while response.status_code >= 400:
            error_data = response.json()
            error_status = error_data['status']
            error = error_data['error']
            print("System returned error with status code: ", error_status, " and error message: ", error)
            id_input = input("Please enter the Ontology ID (or press 'q' to quit): ")
            id_input = id_input.lower()
            if id_input == "q":
                print("Thank you for using the Ontology Lookup Service!")
                exit()
            url = "https://www.ebi.ac.uk/ols4/api/ontologies/" + id_input
            response = requests.get(url)
        data = response.json()

        #Parsing the data to get the title, description, status and number of terms
        config = data['config']
        title = config['title']
        description = config['description']
        status = data['status']
        terms = data['numberOfTerms']

        #Output the parsed data
        #Ask the user if they would like a machine-readable output
        mr_output = input("Would you like a machine-readable output? (yes/no): ")
        mr_output = mr_output.lower()
        if mr_output == "yes":
            ontology_details = {
                    "title": title,
                    "description": description,
                    "number_of_terms": terms,
                    "status": status
                }
            print("")
            print(json.dumps(ontology_details))
            print("")
        else:
            print("")
            print("Title:", title)
            print("Description:", description)
            print("Number of Terms:", terms)
            print("Status:", status)
            print("")

    get_ontology_details(id_input)

