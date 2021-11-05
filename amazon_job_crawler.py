import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.amazon.jobs/en/search?base_query=Software+Development"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


results = soup.find_all(attrs={"data-react-class" : "SearchContent"})

amazon_jobs_search = results[0]['data-react-props']
amazon_jobs_search_json = json.loads(amazon_jobs_search)

print(json.dumps(amazon_jobs_search_json["business_categories_cms"],indent=4, sort_keys=True))
