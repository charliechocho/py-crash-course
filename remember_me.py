import json

username = input('Vad är ditt användarID?: ')

filename = 'user_db.json'

with open(f'txt_files/{filename}', 'w') as f:
    json.dump(username, f)
    print(f"Vi kommer komma ihåg dig när du kommer tillbaks {username}")