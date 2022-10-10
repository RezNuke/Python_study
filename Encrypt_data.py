#import simplecrypt
import pip
file_info_path = 'D:\Programming\Stepik_course\Readable files\encrypted.bin'
file_password_path = 'D:\Programming\Stepik_course\Readable files\passwords.txt'

with open(file_info_path, "rb") as inf:
    encrypted = inf.read()




with open(file_password_path, "r") as psw:
    for line in psw:
        password = line.strip('\n')
        print(password)

    
#     try: 
#         inf = simplecrypt.decrypt(password, encrypted)





# inf = simplecrypt.decrypt(data = encrypted, password = 'RVrF2qdMpoq6Lib')
# print(inf)
