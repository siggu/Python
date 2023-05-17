from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)


def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs?q="
  browser.get(f"{base_url}{keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", class_="ecydgvn0")
  pages = pagination.find_all("div", class_="ecydgvn1")
  if not pages:
    return 1
    count = len(pages)
  if count >= 5:
    return 5
  else:
    return count


print(get_page_count("python"))
print(get_page_count("next js"))
print(get_page_count("jango"))
print(get_page_count("nest js"))
print(get_page_count("java"))
print(get_page_count("react"))


def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)
  for page in range(pages):
    base_url = "https://kr.indeed.com/jobs"
    browser.get(f"{base_url}?q={keyword}")
    results = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link': f"https://kr.indeed.com{link}",
          'company': company.string,
          'location': location.string,
          'position': title
        }
        results.append(job_data)
