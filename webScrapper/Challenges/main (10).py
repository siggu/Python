from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")

            job = {
                'company': company.string.rstrip(),
                'position': position.string.rstrip(),
                'location': location.string.rstrip()
            }
            results.append(job)
    else:
        print("Can't get jobs.")
    return results


jobs = extract_jobs("rust")
print(jobs)
