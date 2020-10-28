#Created By SalmanRai
#https://github.com/SalmanRai
#Learn Web Scrapping

import requests
from bs4 import BeautifulSoup
from colorama import Fore

print(Fore.GREEN + "Note : Ngambil sampai 20 halaman")
print("(https://www.vapeclub.co.uk)")
print("Hanya mengambil liquid!", '\n')

url = "https://www.vapeclub.co.uk/search/?sSearchString=Liquid&iPageNumber="

headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
}

count_page = 0
for page in range(1, 21):
    count_page += 1
    print ('Scrapping web', count_page)
    req = requests.get(url, headers = headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    product = soup.findAll('div',class_ = 'productGridItem col-6 col-sm-4 col-md-3 p-1')
for hasil in product:
    nama = hasil.find('h5',class_ = 'mt-3').text
    print(nama)
    harga = hasil.find('div',class_ = 'productGridPrice').text
    print(harga)   
    desc = hasil.find('small').text
    print (desc)
    nikotin = hasil.find('div',class_ = 'nicotineLevels').text
    print('nikotin')