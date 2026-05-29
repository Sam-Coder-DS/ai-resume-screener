import requests
from bs4 import BeautifulSoup
def scrape_job_description(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    lines = [p.get_text().strip() for p in paragraphs]
    clean = [l for l in lines if len(l) > 40]
    return "\n".join(clean)