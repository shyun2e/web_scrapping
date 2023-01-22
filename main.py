from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
browser.get("https://kr.indeed.com/jobs?q=python")
print(browser.page_source)