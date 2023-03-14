import requests, json
import csv

f=  open("D:\Covid 19\crawl so lieu nhiem covid thoi diem chon\output.csv", "w", encoding='UTF8')
writer = csv.writer(f,lineterminator='\n') 

res_api = requests.get('https://static.pipezero.com/covid/data.json')
data_js = res_api.text
dt_js = json.loads(data_js)

header = ["Thành phố", "Số ca chết", "Số ca đang điều trị", "Số ca nhiễm", "Số ca phục hồi", "Số ca nhiễm trong ngày"]
writer.writerow(header)
for i in range(63):

    print('counter',i)
    name = dt_js['locations'][i]['name']
    death = dt_js['locations'][i]['death']
    treating = dt_js['locations'][i]['treating']
    cases = dt_js['locations'][i]['cases']
    recoverd = dt_js['locations'][i]['recovered']
    casesToday = dt_js['locations'][i]['casesToday']
    str1 = [name, death, treating, cases, recoverd, casesToday]
    
    writer.writerow(str1)

f.close()
    