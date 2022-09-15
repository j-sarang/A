from bs4 import BeautifulSoup as bs
import csv
content = []

outfile = open('00_syslog_rules.csv','w')
writer = csv.writer(outfile, lineterminator ="\n")
writer.writerow(["groupname", "rule_id", "level", "pcre2", "description"])

with open('C:/Users/saran/BSoup/syslog_rules.xml', 'r') as f:
    file = f.read()
    bs_file = bs(file, "lxml")
    result = bs_file.find_all("group")
    for i in result:
        print(i.get("name"))

    r2 = bs_file.find_all("rule")
    for i2 in r2:
        print(i2.get("id"))
        print(i2.get("level"))

    r3 = bs_file.find_all("pcre2")
    for i3 in r3:
        print(i3.get_text())

    r4 = bs_file.find_all('description')
    for i4 in r4:
        print(i4.get_text())    

outfile.close()