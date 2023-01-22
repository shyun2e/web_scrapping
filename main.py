from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwwr_jobs

jobs = extract_wwwr_jobs("python")
print(jobs)