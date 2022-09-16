def dlname(pastname):
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup

    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    code = file
    url = 'https://www.dlsite.com/girls/work/=/product_id/' + code
    html  = urllib.request.urlopen(url,context = ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    title = str(soup.h1.string)
    os.rename(file, file + ' ' + title)

import os
files = os.listdir()
print('\n'+'Rename these files：')
for name in files:
    print(name)
print('\n')
errorlist = []
for file in files:
    print('Dealing with '+file+'...')

    if file.startswith('RJ'):
        try:
            dlname(file)
            print('renamed successfully!')
        except:
            print('Unsuccessful!')
            errorlist.append(file)
    elif file.startswith('BJ'):
        try:
            dlname(file)
            print('renamed successfully!')
        except:
            print('Unsuccessful!')
            errorlist.append(file)
    else:
        print(file +' is not dlsite file')
    print('\n')
print('\n Error:')
for name in errorlist:
    print(name)