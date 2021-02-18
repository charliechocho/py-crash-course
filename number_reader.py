import json

filename = 'numbers.json'

with open(f"txt_files/{filename}") as f:
    numbers = json.load(f)

print(numbers)