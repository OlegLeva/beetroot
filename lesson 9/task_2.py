import json

phonebook = [{
    "first_name": "Oleg",
    "last_name": "Levitskiy",
    "phone": +380509000000
}, {
    "first_name": "Nik",
    "last_name": "Levin",
    "phone": +380500000000
}]

f = open('myphonebook.json', 'w')
json.dump(phonebook, f, indent=3)
f.close()



fa = open('myphonebook.json', 'r+')
json_data = json.load(fa)
fn = input("Enter your name: ")
citi_name = input("Enter your citi: ")
region_name = input("Enter your region: ")
for i in json_data:
    if i["first_name"] == fn in i:
        i["citi"] = citi_name
        i["region"] = region_name
        print(i)

