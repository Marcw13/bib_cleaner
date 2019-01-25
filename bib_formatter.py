
# coding: utf-8

import re

bib = open("bib.bib", 'r').read().split('}\n') # specify name/location of bib document here
biblist = []

for line in bib:
    note = ""
    if re.search("@misc{", line):
        misc = line.split('\n')
        for attribute in misc:
            if re.search("url = ", attribute):
                url = attribute
                link = re.findall(r"= {\w+.*",url)
                link = link[0]
                link = re.sub(r"^= {", "", link)
                link = re.sub(r"},$", "", link)
            if re.search("urldate = ", attribute):
                urldate = attribute
                year = re.findall(r"[0-9]{4}",urldate)
                try:
                    year = year[0]
                except:
                    year = "NO YEAR"
                rest = re.findall(r"-[0-9]{2}",urldate)
                try:
                    day = rest[1]
                except:
                    day = "NO DAY"
                day = re.sub(r"-", "", day)
                try:
                    month = rest[0]
                except:
                    month = "NO MONTH"
                month = re.sub(r"-", "", month)
                if month == "01":
                    month = "January"
                elif month == "02":
                    month = "February"
                elif month == "03":
                    month = "March"
                elif month == "04":
                    month = "April"
                elif month == "05":
                    month = "May"
                elif month == "06":
                    month = "June"
                elif month == "07":
                    month = "July"
                elif month == "08":
                    month = "August"
                elif month == "09":
                    month = "September"
                elif month == "10":
                    month = "October"
                elif month == "11":
                    month = "November"
                elif month == "12":
                    month = "December"
                else:
                    month = "NO DATE"
        print link
        note = ",\nnote = {\href{"+ link +"}{"+ link +"} Accessed on: "+ month +" " + day + ", " + year + ".}"
    entry = line + "}" + note + "\n"
    with open("bib_clean.bib","a") as f:
        f.write(entry)
    f.close()
