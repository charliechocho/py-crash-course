glossary = {
    'print':'prints a message to the screen',
    'for_loop':'goes through a list or dictionary and picks up values one by one',
    'if':'looks for conditions and executes commands accordingly',
    'variable':'stores a value for later use',
    'list':'stores a list of values of typ string or num',

}

vokaler = ['a', 'o', 'u', 'å', 'e', 'i', 'y', 'ä', 'ö']

for key, value in glossary.items():
    if key[0] not in vokaler:
        print(f"A {key} command:\n\t {value}")
    else:
        print(f"An {key} command:\n\t {value}")