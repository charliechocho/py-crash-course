users = ['admin','david','alma','FRED','gigi']

users_lower = []

for user in users:
    users_lower.append(user.lower())

new_users = ['earl','alma','goodard','Fred']

if new_users:
    for user in new_users:
        if user.lower() in users_lower:
            print(f"Hello {user.title()}, you seem to be registered already")
        else:
            print(f"Hello {user.title()}, welcome to our site, hope you enjoy it!!")
else:
   print("No new users")