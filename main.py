import requests
from bs4 import BeautifulSoup


def save_login_form(url):

    headers = {
        "Cookie": "rbzid=7vQzhY/Pdww1EGfC/JxsKBDYiY718jmq5PnEK3AHnOayYnJcRIt22IQMptTe34Bb06RmMr9gTe+jznJSqhqMRfJvx113GhhuTs8uMzTfgleUCI0XNVT8iZPmaJShfy8CyNhKwKYJsKUCoFx78R0uq/OsS8Z5lqOcHY6hImWxNS7Rf9bIXjHRnULo/Wt3x3I8eP/blK+5xj6yP4diM8Xr1kqApd5mPJL/doKtQ/TdEOE=; rbzsessionid=b39245f6eca74cee1df2268db7a5f031; ASPSESSIONIDQCCCTSQC=LFELGMNDCKPCJIPBOOGEMMKE",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        login_form = soup.find('form')
        
        # Save or print the HTML of the form
        with open('login_form.html', 'w', encoding='utf-8') as file:
            file.write(str(login_form))
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")


def main():
    url = "https://go.slotimo.com/login/"
    save_login_form(url)

main()