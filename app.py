from bs4 import BeautifulSoup
import requests 
r = requests.get("https://www.hamropatro.com/gold")
r_content = r.content
soup = BeautifulSoup(r_content,"html.parser")
gold_content = soup.find_all("div",{"class":"column6"})
gold_inner_content = gold_content[0].find_all("ul")
i = 0
while i<=5 :
    gold_title = gold_inner_content[0].find_all("li")[i*2].text.replace("\n","")
    gold_price = gold_inner_content[0].find_all("li")[i*2+1].text.replace("\n","")
    gold = gold_title + " " + gold_price
    print(gold)
    i=i+1
    
    