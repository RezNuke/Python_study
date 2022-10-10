import requests
import re


Test = 'https://raw.githubusercontent.com/cr00z/cr00z/main/temp/test_stepik.txt'
site_set = set()

pattern_url = r'a[\s]*href=[\'|\"]([\S]*)[\'|\"]'
pattern_site = r'(\w)(\w*\.\w*\.?\w*)'

html_a = requests.get(Test)
if html_a.status_code == 200:
    url = re.findall(pattern_url, html_a.text)
    for i in url:
        site = re.search(pattern_site, i)
        try:
            if site.group(1) is not None:
                site_set.add(site.group(1) + site.group(2))
        except:
            pass
        
for i in site_set:
    print(i)