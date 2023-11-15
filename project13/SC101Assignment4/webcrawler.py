"""
File: webcrawler.py
Name: Angela
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all("tbody")

        m_number = 0
        f_number = 0

        for tag in tags:
            info = tag.get_text()
            tokens = info.split()
            for i in range(200):
                tokens[2 + 5*i] = remove_comma(tokens[2 + 5*i])
                tokens[4 + 5*i] = remove_comma(tokens[4 + 5*i])
                m_number += int(tokens[2 + 5*i])
                f_number += int(tokens[4 + 5*i])

        print("Male Number: " + str(m_number))
        print("Female Number: " + str(f_number))


def remove_comma(string):
    ans = ""
    for ch in string:
        if ch.isdigit():
            ans += ch

    return ans



if __name__ == '__main__':
    main()
