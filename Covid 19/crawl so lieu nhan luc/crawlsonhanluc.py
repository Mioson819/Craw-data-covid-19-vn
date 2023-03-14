import csv
import openpyxl
 

write = open(r"D:\Covid 19\crawl so lieu nhan luc\nhanluc.csv", "w", encoding='UTF8')
writer = csv.writer(write, lineterminator='\n')
header = ["Thành phố","Bác sĩ","Y Tá"]
writer.writerow(header)


f_read = openpyxl.load_workbook('D:\Covid 19\crawl so lieu nhan luc\Số liệu nhân lực.xlsx')


sheet  = f_read['Trang tính1']

data= sheet['A1:D71']


for i in  range(71):
    tinh = data[i][0].value
    if tinh == 2021:
        continue
    if tinh == "CẢ NƯỚC":
        continue
    if tinh == "Đồng bằng sông Hồng":
        continue
    if tinh == "Trung du và miền núi phía Bắc":
        continue
    if tinh == "Bắc Trung Bộ và Duyên hải miền Trung":
        continue
    if tinh == "Đông Nam Bộ":
        continue
    if tinh == "Đồng bằng sông Cửu Long":
        continue
    
    bs = data[i][1].value
    yta = data [i][3].value
    str1 = {tinh:1,bs:2,yta:3}
    print(str1)
    writer.writerow(str1)
    
write.close()