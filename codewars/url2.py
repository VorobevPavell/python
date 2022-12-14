def domain_name(url):
    url = url.replace('http://','')
    url = url.replace('https://','')
    url = url.replace('www.','')
    url = url.split('.')
    return url[0]

print(domain_name("https://www.cnet.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("https://youtube.com"))
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))