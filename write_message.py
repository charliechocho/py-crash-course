filename = 'programming.txt'
file_path = 'txt_files/'

with open(f'{file_path}{filename}', 'w') as file_obj:
    for i in range(11):
        file_obj.write('I Love Python more than anything!!\n')
