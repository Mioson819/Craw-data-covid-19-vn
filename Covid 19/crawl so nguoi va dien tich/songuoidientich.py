import requests
from bs4 import BeautifulSoup
import csv

f=  open("D:\Covid 19\crawl so nguoi va dien tich\songuoi_dientich.csv", "w", encoding='UTF8')
writer = csv.writer(f,lineterminator='\n')
header = ["Thành phố", "Diện tích", "Dân số"]
writer.writerow(header)

link = "https://meta.vn/huong-dan/tong-hop/dien-tich-va-dan-so-cac-tinh-viet-nam-10058"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
tb = soup.find_all('table')
tr = tb[0].find_all("tr")

list = [1, 2, 3]
for row in tr[1:]:
    
    td =row.find_all('td')
    tinh = td[1].p.text
    dt = td[2].p.text.replace(",",".")
    ds = td[3].p.text.replace(".","")
    str1= {tinh:1, dt:2, ds:3}
    print(str1)    
    writer.writerow(str1)
       
f.close()