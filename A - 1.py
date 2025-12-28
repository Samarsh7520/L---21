info = {
    "id1":{"Name":"Samarsh","Roll":12},
    "id2":{"Name":"Vivvan","Roll":13},
    "id3":{"Name":"Kiyansh","Roll":14},
    "id4":{"Name":"Aarav","Roll":15},
    "id5":{"Name":"Samarsh","Roll":12},
}
result = {} 
for key,value in info.items():
    if value not in result.values():
        result[key] = value

print(result)