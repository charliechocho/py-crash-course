responses = {}

#setting active flag

polling_active = True

while polling_active:
    #Prompt a user for their name and ask about a mountain they'd like to climb

    name = input("\nWhat is your name? ")
    mountain = input("\nWhat mountain would you climb, given the chance? ")

    responses[name] = mountain

    question = input("Would you like for someone else to answer the question? ")
    if question == 'no':
        polling_active = False

print("\n--- Polling Results ---")

for name, response in responses.items():
    print(f"{name} would liket to climb {response}")
