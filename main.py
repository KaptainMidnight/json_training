import json

filename = "settings.json"
myfile = open(filename, 'w', encoding="Latin-1")

buyer_1 = {
    "name": "Adidas",
}

buyer_2 = {
    "name": "Nike"
}

buyer_3 = {
    "name": "Adidas",
    "name_2": "Nike"
}

buyer_4 = {
    "name": "Adidas",
    "name_2": "Reebok"
}

sells = []
sells.append(buyer_1)
sells.append(buyer_2)
sells.append(buyer_3)
sells.append(buyer_4)
#  Save JSON
json.dump(sells, myfile, indent=2, ensure_ascii=False)
myfile.close()
