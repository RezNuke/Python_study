import simplecrypt
file_info_path = 'D:\Programming\Stepik_course\Readable files\encrypted.bin'

with open(file_info_path, "rb") as inp:
    encrypted = inp.read()

file_pass_path = 'D:\Programming\Stepik_course\Readable files\passwords.txt'

'''
with open(file_pass_path, "rb") as psw:
    password = psw.read()
    print(password)
    try: 
        inf = simplecrypt.decrypt(password, encrypted)
'''



