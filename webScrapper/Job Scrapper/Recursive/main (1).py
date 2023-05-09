from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

# indeed 에서 remoteok로 사이트 변경
browser.get("https://remoteok.com/remote-python-jobs")

soup = BeautifulSoup(browser.page_source, "html.parser")
