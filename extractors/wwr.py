from requests import get
from bs4 import BeautifulSoup

def extract_wwwr_jobs(keyword):
  

  base_url = "https://weworkremotely.com/remote-jobs/search?%E2%9C%93&term="
  
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website!")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all("li")
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')  #<a> 얻기 위에
        anchor = anchors[1]  #html 코드를 보면 두 번째 href가 우리가 원하는 코드.
        link = (anchor['href'])#beautifulsoup 은 아름답게 dictionary형식으로 저장
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_="title")#find_all은 list,find는 결과
  
        job_data = {
          'link': f"https://weworkremotely.com/{link}",
          'company': company.string,
          'region': region.string,
          'position': title.string
        }
        results.append(
          job_data
        )  # <<<< 하는 이유? for loop안에서 job_data는 계속 재생성하기에 전 데이터들은 사라지게 될 것임.
    return results