import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


def save_login_form():

    url = "https://go.slotimo.com/login/"

    headers = {
        "Cookie": "rbzid=7vQzhY/Pdww1EGfC/JxsKBDYiY718jmq5PnEK3AHnOayYnJcRIt22IQMptTe34Bb06RmMr9gTe+jznJSqhqMRfJvx113GhhuTs8uMzTfgleUCI0XNVT8iZPmaJShfy8CyNhKwKYJsKUCoFx78R0uq/OsS8Z5lqOcHY6hImWxNS7Rf9bIXjHRnULo/Wt3x3I8eP/blK+5xj6yP4diM8Xr1kqApd5mPJL/doKtQ/TdEOE=; rbzsessionid=b39245f6eca74cee1df2268db7a5f031; ASPSESSIONIDQCCCTSQC=LFELGMNDCKPCJIPBOOGEMMKE",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        login_form = soup.find('form')
        
        with open('login_form.html', 'w', encoding='utf-8') as file:
            file.write(str(login_form))
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")


def get_promotions(proxy={}):
    

    url = "https://www.woocasino.com/promotions"

    response = requests.get(url, proxies={"http": proxy, "https": proxy})

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        promotions = soup.find_all('div', class_='promotions-single__content')

        with open('promotions.txt', 'w', encoding='utf-8') as file:
            for promo in promotions:
                title = promo.find('h2').get_text() if promo.find('h2') else 'No title'
                description = promo.find('p').get_text() if promo.find('p') else 'No description'
                file.write(f"Title: {title}\n")
                file.write(f"Description: {description}\n")
                file.write('---' * 10 + '\n')

        print("Promotions have been written to promotions.txt")
    else:
        print(f"Failed to request. Status code: {response.status_code}")


def get_bonuses():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = 'https://betandyou-227625.top/pl/bonus/rules'
        page.goto(url)

        page.wait_for_selector('.bonuses-bonus-tile__content')

        html_content = page.content()

    soup = BeautifulSoup(html_content, 'html.parser')
    titles = soup.find_all('div', class_='template-compiler bonuses-bonus-tile-name__compile')

    with open('bonuses.txt', 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title.get_text(strip=True)+"\n")


def main():
     
    save_login_form()
    proxy = "http://173.249.39.200:3128" # Change to your working DE proxy to test
    get_promotions(proxy)
    get_bonuses()



main()