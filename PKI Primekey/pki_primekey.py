from urllib.request import urlopen
from bs4 import BeautifulSoup
#This code is for the first set of troubleshotting events under Startup roblems in CICS

# index = [10,20,30,40,50,60,70,80,90,100,110]
# for l in index:
#     URL = ('https://doc.primekey.com/dosearchsite.action?cql=label+%3D+%22ejbca-troubleshooting%22&startIndex='+str(l))
#     soup = BeautifulSoup(urlopen(URL), features='lxml')

#     #https://doc.primekey.com/dosearchsite.action?cql=label+%3D+%22ejbca-troubleshooting%22&startIndex=10
#     result = soup.select('a.search-result-link')
#     for r1 in result:
#         r2 = []
#         k = (r1.get('href')).replace('/display','https://doc.primekey.com/display/')
#         r2.append(k)
#         print(r2)

    
r3 = ['https://doc.primekey.com/display//EJBCA731/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCA731/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA731/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA731/Publishing',
    'https://doc.primekey.com/display//EJBCA731/Validation+Authority',
    '/pages/viewpage.action?pageId=9047210',
    'https://doc.primekey.com/display//EJBCA740/Cryptography+and+Security',
    '/pages/viewpage.action?pageId=9048504',
    'https://doc.primekey.com/display//EJBCA740/Publishing',
    'https://doc.primekey.com/display//EJBCA740/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA740/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA740/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA741/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCA741/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA741/Enrollment+Questions',
    '/pages/viewpage.action?pageId=16683914',
    'https://doc.primekey.com/display//EJBCA741/Publishing',
    'https://doc.primekey.com/display//EJBCA741/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA742/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA742/Publishing',
    '/pages/viewpage.action?pageId=16686804',
    'https://doc.primekey.com/display//EJBCA742/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA742/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA742/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCA743/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA743/Publishing',
    '/pages/viewpage.action?pageId=16687990',
    'https://doc.primekey.com/display//EJBCA743/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA743/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA743/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCADS/Installation+and+Deployment',
    '/pages/viewpage.action?pageId=6029885',
    'https://doc.primekey.com/display//EJBCADS/PKI+Management',
    'https://doc.primekey.com/display//EJBCADS/Publishing',
    'https://doc.primekey.com/display//EJBCADS/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA750/PKI+Management',
    'https://doc.primekey.com/display//EJBCA750/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCA750/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA750/Enrollment+Questions',
    '/pages/viewpage.action?pageId=16689285',
    'https://doc.primekey.com/display//EJBCA750/Publishing',
    'https://doc.primekey.com/display//EJBCA750/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA750/Troubleshoot+Database+Performance',
    'https://doc.primekey.com/display//EJBCA760/PKI+Management',
    'https://doc.primekey.com/display//EJBCA760/Troubleshoot+Database+Performance',
    'https://doc.primekey.com/display//EJBCA760/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA760/Publishing',
    'https://doc.primekey.com/display//EJBCA60/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA760/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA760/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCADS/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCADS/Troubleshoot+Database+Performance',
    'https://doc.primekey.com/display//EJBCA770/PKI+Management',
    'https://doc.primekey.com/display//EJBCA770/Troubleshoot+Database+Performance',
    'https://doc.primekey.com/display//EJBCA770/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA770/Publishing',
    'https://doc.primekey.com/display//EJBCA770/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA770/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA770/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCA780/PKI+Management',
    'https://doc.primekey.com/display//EJBCA780/Troubleshoot+Database+Performance',
    'https://doc.primekey.com/display//EJBCA780/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA780/Publishing',
    'https://doc.primekey.com/display//EJBCA780/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCA780/Installation+and+Deployment',
    'https://doc.primekey.com/display//EJBCA780/Cryptography+and+Security',
    'https://doc.primekey.com/display//EJBCA781/PKI+Management',
    'https://doc.primekey.com/display//EJBCA781/Troubleshoot+Database+Performance',
    'https://doc.primekey.com/display//EJBCA781/Validation+Authority',
    'https://doc.primekey.com/display//EJBCA781/Publishing',
    'https://doc.primekey.com/display//EJBCA781/Enrollment+Questions',
    'https://doc.primekey.com/display//EJBCADS/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA750/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA760/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA770/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA780/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA781/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA790/Command+Line+Interface',
    'https://doc.primekey.com/display//EJBCA791/Command+Line+Interface']


  

def myfunc(x):
        c = 0
        for c in range(0,2):
                soup2 = BeautifulSoup(urlopen(str(x[c])), features='lxml')
                x2 = soup2.find('h1',class_="cell article__heading")
                print(x2)
                x3 = soup2.find_all('h2')
                print(x3)
                x4 = soup2.find_all('p')
                print(x4)
                c +=1
                if c == len(x) + 1:
                    break
                else:
                    continue

myfunc(r3)






