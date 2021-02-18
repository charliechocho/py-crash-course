filenames = ['cats.txt', 'dogs.tx']
file_path = 'txt_files/'

for file in filenames:
    try:
        with open(f"{file_path}{file}", encoding = 'utf-8') as f:
            text = f.read()
            print(text)

    except FileNotFoundError:
        pass