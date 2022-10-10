import os
import os.path

path = 'D:\Programming\Stepik_course\Readable files\File_directory.txt'

os.chdir('D:\Programming\Stepik_course\Readable files\main')

with open(path, 'w') as f:
    pass

file_path = []
status_py = False

for current_dir, dirs, files in os.walk('.'):
    status_py = False
    for file_ in files:
        if file_.find('.py') != -1:
            status_py = True
            break
    if status_py:
        file_path.append(f'{current_dir[2:]}\n'.replace('/', '\\'))
        continue
                
file_path.sort()

with open(path, 'a') as f:
    for el in file_path:
        f.writelines(el)
        
print(len(file_path))