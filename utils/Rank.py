import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import openpyxl
import json
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

MAX_RESULTS = 100  # up to 100 results (Google usually returns 10 per page)
RESULTS_PER_PAGE = 10

def load_keywords_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    return [row[0].value for row in sheet.iter_rows(min_row=2) if row[0].value]

def fetch_ranking(keyword, domain):
    keyword_encoded = keyword.replace(" ", "+")
    for start in range(0, MAX_RESULTS, RESULTS_PER_PAGE):
        url = f"https://www.google.com/search?q={keyword_encoded}&start={start}"
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
        except Exception as e:
            return {keyword: {"error": str(e)}}

        if response.status_code != 200:
            return {keyword: {"error": f"Status {response.status_code}"}}

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='yuRUbf')

        for i, result in enumerate(results):
            link = result.find('a')['href']
            rank = start + i + 1
            if domain in link:
                return {keyword: {"rank": rank, "url": link}}

        time.sleep(1.0)  # avoid getting blocked

    return {keyword: {"rank": None, "url": None}}

def check_website_ranking_parallel(keywords, domain):
    results = {}

    def process_keyword(keyword):
        return fetch_ranking(keyword, domain)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = executor.map(process_keyword, keywords)
        for result in futures:
            results.update(result)

    return results

def check_rank():
    keywords = load_keywords_from_excel("Z:\\CMD\\Script\\keywords.xlsx")
    domain = "shashaschoice.com"
    results = check_website_ranking_parallel(keywords, domain)
    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    check_rank()
