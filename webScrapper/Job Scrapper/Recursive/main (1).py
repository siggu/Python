from requests import get
from bs4 import BeautifulSoup

base_url = "https://remoteok.com/remote-"
search_term = "python-jobs"

headers = {
  "User-Agent":
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
} # 헤더 추가

response = get(f"{base_url}{search_term}", headers=headers)

if response.status_code != 200:
  print("Can't request page")
  print(response.status_code)
else:
  soup = BeautifulSoup(response.text, "html.parser")
