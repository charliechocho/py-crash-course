file_path = 'txt_files/'
file_name = 'python_learning.txt'

with open(f'{file_path}{file_name}') as file_obj:
    file_lines = file_obj.readlines()

    
for line in file_lines:
    print(line.replace('Python', 'Go-Lang'))

