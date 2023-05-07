# https://weworkremotely.com/
"""
1. 파이썬을 이용해 사이트에 접속하기
"""

from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Can't request website")
else:
  print(response.text)
