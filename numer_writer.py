import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(f'txt_files/{filename}', 'w') as f:
    json.dump(numbers, f)

