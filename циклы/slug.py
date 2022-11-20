t = ['a','b','v','g','d','e','zh','z','i','y','k','l','m','n','o','p','r','s','t','u','f','h','c','ch','sh','shch','','y','','e','yu','ya']


start_index = ord('а')
slug = ' '
title = 'Программирование на Пайтон - лучший курс!'
for i in title.lower():
    if 'а' <= i <= 'я':
        slug += t[ord(i) - start_index]
    elif i in ' ;:!?':
        slug += '-'


while slug.count('--'):
    slug = slug.replace('--','-')
print(slug)