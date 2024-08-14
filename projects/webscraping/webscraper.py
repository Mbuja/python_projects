from bs4 import BeautifulSoup as bs
import requests

def scrape()->requests:
    #r=requests.get("https://49s.co.uk/49s/results")
    r = requests.get("https://49s.events/lunchtime")
    return r


def extract_dates(soup:bs):
    data = soup.find_all('tr')
    headers =[]
    for var in data:
        if(var.td):
            headers.append(str(var.td.get_text().strip()))
    #print(headers)
    return headers


def extract_numbers(soup:bs):
    data = soup.find_all('div',class_ = 'result')
    numbers = []
    num_lists =[]
    for num in data:
        if num:
            numbers.append(int(num.get_text()))
    while(len(numbers)!=0):
        temp_list = numbers[0:7]
        num_lists.append(temp_list)
        numbers = numbers[7::]
    #print(num_lists)
    return num_lists

if __name__ == "__main__":
    response = scrape()
    soup = bs(response.content,'html.parser')
    content = soup.find_all('tr')
    extract_dates(soup)
    extract_numbers(soup)
    print(dict(zip(extract_dates(soup),extract_numbers(soup))))
    #print(content)