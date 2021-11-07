import requests
import json
from bs4 import BeautifulSoup

URL = "https://careers.google.com/api/v3/search/?category=DATA_CENTER_OPERATIONS&category=DEVELOPER_RELATIONS&category=HARDWARE_ENGINEERING&category=INFORMATION_TECHNOLOGY&category=MANUFACTURING_SUPPLY_CHAIN&category=NETWORK_ENGINEERING&category=PRODUCT_MANAGEMENT&category=PROGRAM_MANAGEMENT&category=SOFTWARE_ENGINEERING&category=TECHNICAL_INFRASTRUCTURE_ENGINEERING&category=TECHNICAL_SOLUTIONS&category=TECHNICAL_WRITING&company=Google&company=YouTube&q="
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
site_json=json.loads(soup.text)
for job in site_json['jobs']:
    print(job['title'])
