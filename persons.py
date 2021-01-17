persons_0 = {
    'first_name':'nina',
    'last_name':'pentti',
    'age':'54',
    'city':'uppsala',
}
persons_1 = {
    'first_name':'mattias',
    'last_name':'söderberg',
    'age':'51',
    'city':'uppsala',
}

persons_2 = {
    'first_name':'robin',
    'last_name':'söderberg',
    'age':'27',
    'city':'rosendal',
}

adress_book = [persons_0, persons_1, persons_2]

for people in adress_book:
        name = f"{people['first_name']} {people['last_name']}"
        age = people['age']
        geo = people['city']
        print(f"I know {name.title()} who is {age} years old and lives in {geo.title()}!\n")



# print(f"{persons['first_name']} {persons['last_name']} is my my favorite person. "
#     f"She's {persons['age']} years old and lives in {persons['city']}")

# for key in persons:
#     print(f"\nKey: {key}")
# #    print(f"Value: {value}")