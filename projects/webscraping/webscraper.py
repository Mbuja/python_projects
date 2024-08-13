from bs4 import BeautifulSoup as bs
import requests

def scrape()->requests:
    #r=requests.get("https://49s.co.uk/49s/results")
    r = requests.get("https://49s.events/lunchtime")
    return r

if __name__ == "__main__":
    response = scrape()
    soup = bs(response.content,'html.parser')
    content = soup.find_all('tr')
    print(content)