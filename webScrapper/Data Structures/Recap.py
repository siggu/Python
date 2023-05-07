from requests import get

websites = ("google.com", "airbnb.com", "https://twitter.com", "facebook.com",
            "https://tiktok.com")

results = {}

for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  response = get(website)

  if response.status_code >= 500:
    results[website] = "server error"
  elif response.status_code >= 400:
    results[website] = "client error"
  elif response.status_code >= 300:
    results[website] = "redicrection"
  elif response.status_code >= 200:
    results[website] = "good"
  else:
    results[website] = "ok"

print(results)
