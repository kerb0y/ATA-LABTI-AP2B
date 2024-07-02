import json

file_json = open('act2.json')

data = json.loads(file_json.read())

print('--------------------------------------\n')

for i in range(len(data)):
    print(f"Nama        : {data[i]['nama']}")
    print(f"NPM         : {data[i]['npm']}")
    print(f"Kelas       : {data[i]['kelas']}")
    print(f"Fakultas    : {data[i]['fakultas']}")
    print(f"Jurusan     : {data[i]['jurusan']}")
    print()