from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

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


def plot_histogram(keys,data):
    #pd.DataFrame(keys,data)
    dic = dict(zip(keys,data))
    #a = pd.Series(dic)
    a = pd.DataFrame(dic)
    values =[]
    for x in data:
        values.extend(x)
    print(values)
    plt.hist(values,bins=50,range=(1,50),edgecolor ='black')
    plt.xlabel("Lucky Number")
    plt.ylabel("Frequency")
    plt.show()
    #print(a)
    #pd.DataFrame({'A':[1,2,3]})


def plot_bar(keys,data):
    values = []
    for x in data:
        values.extend(x)
    counts = Counter(values)
    x_points = range(1,50)
    y_points = [counts.get(x,0) for x in x_points]
    plt.bar(x_points,y_points,color ='green',edgecolor ='black')
    plt.xticks(range(1,50))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Lucky Number Frequency bar graph')
    plt.show()


if __name__ == "__main__":
    response = scrape()
    soup = bs(response.content,'html.parser')
    content = soup.find_all('tr')
    keys = extract_dates(soup)
    data = extract_numbers(soup)
    #print(dict(zip(extract_dates(soup),extract_numbers(soup))))
    #print(content)
    plot_bar(keys,data)