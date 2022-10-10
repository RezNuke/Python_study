import requests
url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
url_txt = 'https://stepic.org/media/attachments/course67/3.6.3/'

r = requests.get(url)
x = r.text
i = 0

while x[:2] != 'We':
    if x[:2] != 'We': 
        r = requests.get(url_txt + x)
        x = r.text
        i += 1


print(i)        
print(x) 