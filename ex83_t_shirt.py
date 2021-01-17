def t_shirt_type(size = 'large', text_mess = 'One Awesome Tee'):
    """Behandla beställning av storlek och text på t-shirt"""
    print(f"One order of a {size.title()} t-shirt")
    print(f"The text on the Tee will be {text_mess.title()}")

t_shirt_type()