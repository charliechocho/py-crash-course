import json

def get_user():
    """Get the users name if it exists"""

    filename = 'user_db.json'
    
    try:
        with open(f'txt_files/{filename}') as f:
            username = json.load(f)

    except FileNotFoundError:
        return None

    else:
        return username

def create_new_user():
    """Prompt user to enter desired username"""
    username = input('Vad är ditt användarID?: ')
    filename = 'user_db.json'
    
    with open(f'txt_files/{filename}', 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet user by name"""
    username = get_user()

    if username:
        print(f"Välkommen tillbaks {username.title()}!!")
    else:
        username = create_new_user()
        print(f"Vi kommer ihåg dig när du återvänder {username}")        
        

greet_user()