users = {
    'smattias':{
    'name':'mattias',
    'fam_name':'söderberg',
    'location':'uppsala',
    },

    'apaul':{
    'name':'paul',
    'fam_name':'andersson',
    'location':'spånga',
    },

    'hpeter':{
    'name':'peter',
    'fam_name':'holmström',
    'location':'göteborg',
    },
}

for username, user_info in users.items():
    print(f"Username: {username}:")
    full_name = f"{user_info['name']} {user_info['fam_name']}"
    geo = f"{user_info['location']}"

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {geo.title()}")
