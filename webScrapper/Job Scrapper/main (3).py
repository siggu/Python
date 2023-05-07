# https://weworkremotely.com/
"""
1. 파이썬을 이용해 사이트에 접속하기
2. jobs 라는 class를 가진 section 찾기
3. section 안에 있는 ul 안의 li만 가져오기
"""
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all("section", class_="jobs")

  for job_section in jobs:
    job_posts = job_section.find_all("li")
    job_posts.pop(-1)
    for post in job_posts:
      print(post)
      print()