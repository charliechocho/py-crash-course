def greet_user(user, lastname):
    """Display a simple greeting with two parameters"""
    full_name = f"{user} {lastname}"
    print(f"Hello! {full_name.title()}")

greet_user('sarah', 'mcdonald')