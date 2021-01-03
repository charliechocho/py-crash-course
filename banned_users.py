banned_users = ['david','bowie','tom']

user = 'david'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish!")
else:
    print(f"You are not a registered user {user.title()}.\
 Please register to post!")

