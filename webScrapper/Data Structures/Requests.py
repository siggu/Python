# pypi.org
# requests: python 코드에서 웹사이트로 request 보내는 걸 할 수 있게 해줌
from requests import get

websites = ("google.com", "airbnb.com", "https://twitter.com", "facebook.com",
            "https://tiktok.com")

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  print(website)
