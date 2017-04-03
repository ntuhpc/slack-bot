import requests
from lxml import html

def check_isc17_coding_challenge():
    """
    Checks whether the coding challenge for ISC17 has been released
    """
    benchmark_page_url = "http://hpcadvisorycouncil.com/events/student-cluster-competition/Benchmarking/"
    page = requests.get(benchmark_page_url)
    if page.status_code == 200:
        tree = html.fromstring(page.content)
        coding_challenge_info = str(tree.xpath('//*[@id="posts-list"]/article/div[2]/p[3]/text()')[0])
        return "Coding challenge: " + coding_challenge_info
    else:
        return "Webpage inaccessible"
