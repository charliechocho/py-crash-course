rivers = {'nissan':'sweden', 'thamse':'england', 'seine':'france'}

eu_rivers = ['nissan', 'seine']

for key, value in rivers.items():
    if key in eu_rivers:
        print(f"The {key.title()} runs through {value.title()} and is part of "
            f"the EU")
    else:
        print(f"The {key.title()} runs through {value.title()}, not in the EU")

for key in rivers:
    print(key.title())

for value in rivers.values():
    print(value.title())