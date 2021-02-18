filenames = ['alice.txt', 'siddharta.py', 'moby_dick.txt', 'little_women.txt']
file_path = 'txt_files/'


def count_words(filename):
    """Function to count words in a file"""
    try:
        with open(f"{file_path}{filename}", encoding = 'utf-8') as f:
            contents = f.read()


    except FileNotFoundError:
        pass
        #print(f"I can't seem to find the {filename} file in this directory")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file, {filename} has about {num_words} words!")

#Get the number of words in textfiles by calling count_words function
for filename in filenames:
    count_words(filename)