#------------------------------------------------
# main.py
# settings.json
# venv
# readme.md
#
# json_training
#
# Created by Alex Artemkin on 24/01/2019.
# Copyright © 2019 Alex Artemkin. All rights reserved.
#----------------------------------------------- 

import json  # Import module json

'''Create file and open him'''
filename = "settings.json"  # Create json file
myfile = open(filename, 'w', encoding="utf-8")  # Open file settings.json
'''Create dictionary'''
customer_1 = {  # First customer and his basket
    "name": "Adidas",
}

customer_2 = {  # Second customer and his basket
    "name": "Nike"
}

customer_3 = {  # Third customer and his backet
    "name": "Adidas",
    "name_2": "Nike"
}

customer_4 = {  # Fourth customer and his basket
    "name": "Adidas",
    "name_2": "Reebok"
}
'''Insert in list choice'''
choice = []  # Choice customers
choice.append(customer_1)  # Add in list first customer with his basket
choice.append(customer_2)  # Add in list second customer with his basket
choice.append(customer_3)  # Add in list third customer with his basket
choice.append(customer_4)  # Add in list fourth customer with his basket
#  Save JSON
json.dump(choice, myfile, indent=2, ensure_ascii=False)  # Save in file settings.json
myfile.close()  # Close file

#  Read and Load file settings.json

my_json = open(filename, 'r', encoding='utf-8')  # Open file settins.json
json_data = json.load(my_json)  # Load file settings.json in variable json_data
print(data_json)  # Print variable json_data
