import requests
from bs4 import BeautifulSoup


def blog_crawling():
    url = "https://search.naver.com/search.naver"
    query = {"query": "참치", "sm":"tab_jum", "where":"post"}

    response = requests.get(url, params=query)

    print(response)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    blog_post_list = []

    for links in soup.select('li.sh_blog_top > dl'):
        title = links.select('dt > a')
        content = links.select('dd.sh_blog_passage')
        author = links.select('dd.txt_block a')

        title = title[0].get('title')
        content = content[0].text
        author = author[0].text
        blog_post = {'author': author, 'title': title, 'content': content}  # 블로그 데이터를 사전으로 만들어주었습니다.

        blog_post_list.append(blog_post)
    return blog_post_list

blog_post_list = blog_crawling()
print(blog_post_list)