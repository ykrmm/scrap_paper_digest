import requests
from bs4 import BeautifulSoup
import re
import argparse

parser = argparse.ArgumentParser(description="Scrapping Paper digest")
parser.add_argument("--url", type=str,help="URL paper digest of a highlights conf")
parser.add_argument('-w', '--key_word', nargs='+', default=[])
parser.add_argument("--all", action='store_true', default=False, help="All keyword must match, default: False.")
parser.add_argument("--search_highlights", action='store_true', default=False, help="Search keyword in highlights to")


args = parser.parse_args()
vgm_url = args.url
key_word = args.key_word
hlt_search = args.search_highlights
all_words = args.all

html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
#print('here')
list_tr = soup.find_all("tr")
cpt = 0


for i,paper in enumerate(list_tr):
    if i > 0: 
        list_td = paper.find_all("td")
        paper = list_td[1]
        title = paper.find("b").text
        highlight = paper.find("i").text
        
        if hlt_search:
            search = title+' '+highlight
        else:
            search = title
        #import ipdb; ipdb.set_trace()
        if all_words:
            display = all(word in search.lower() for word in key_word)
        else:
            display = any(word in search.lower() for word in key_word)

        if display:
            print(title)
            print('\n')
            print(highlight)
            print('\n')
            cpt+=1
            
        
print(cpt,"Papers found matching your search")
