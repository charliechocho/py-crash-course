nonverified_users = ['calvin klein','ralph lauren','christian dior','donna karran']
verified_users = []

#verifying if there are new users and moving them to a verified list
while nonverified_users:
    current_user = nonverified_users.pop()
    print(f"\nVerifying user: {current_user}")
    verified_users.append(current_user)

#Printing out the verified users
for user in verified_users:
    print(f"\n\t{user.title()} is now verfied!")