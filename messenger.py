def show_message(messages_li):
    """Display messages from a list"""
    while messages_li:
        msg = messages_li.pop()
        msg_archive.append(msg)

    msg_archive.reverse()



msg_store = ['Hej på dig', 'Hur mår du?', 'Katter är coola', 'Hundar är tröga']
msg_archive= []

show_message(msg_store[:])
for messages in msg_archive:
    print(messages)

print(msg_store)