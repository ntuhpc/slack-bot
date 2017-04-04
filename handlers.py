import random
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

def pick_a_quotation():
    """
    Randomly picks a quotation
    """
    quotations = [
            "🐒啊",
            "你问我滋磁不滋磁",
            "你们还要学习一个",
            "我是身经百战，见得多了",
            "西方的哪一个国家我没去过",
            "美国的华莱士比你们不知道高到哪里去了，我跟他谈笑风生",
            "媒体还是要提高自己的姿势水平",
            "你们有一个好，全世界跑到什么地方，你们比其他的西方记者跑得还快",
            "too young, too simple, sometimes naïve",
            "我有必要告诉你们一点人生的经验",
            "中国有一句话叫“闷声发大财／大发财”，这是坠吼的",
            "如果将来宣传报道有偏差，你们要负责",
            "你们啊，不要想喜欢弄个大新闻，说现在已经钦定了，再把我批判一番",
            "后来我就念了两句诗，叫“苟利国家生死以，岂因祸福避趋之”",
            "很惭愧，就做了一点微小的工作，谢谢大家",
            "你们给我搞的这本东西，excited！",
            "这个报告经过好几百个教授一致通过"
    ]
    return random.choice(quotations)
