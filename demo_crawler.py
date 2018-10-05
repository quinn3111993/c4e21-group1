import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import requests
import random
import mlab
from quote import Quote

browser = webdriver.Chrome('/Users/quinn/Downloads/chromedriver')
mlab.connect()

quotes = []

def get_topic():
    url = "https://www.brainyquote.com/topics"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    topic_list = [a.span.string for a in soup.find_all('a', 'topicIndexChicklet')]
    chars = ["'", " "]
    for char in chars:
        topic_list = [topic.replace(char,'').lower() for topic in topic_list]
    return topic_list


def get_quotes(topic):
    url = "http://www.brainyquote.com/quotes/topics/topic_" + topic
    browser.get(url)
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 80 #number of actual page down = n/4

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

    for i in range(1,21):
        for j in range(1,27):
            id = 'qpos_{0}_{1}'.format(str(i),str(j))
            print(id)
            quote_elems = browser.find_elements_by_id(id)
            for quote in quote_elems:
                lines = quote.text.splitlines()
                content = lines[0]
                author = lines[1]
                dic = {
                    "content": content,
                    "author": author,
                    "topic": topic,
                }
                print(dic)
                # quotes.append(dic)
                new_quote = Quote(topic=topic, author=author, content=content, priority=0)
                new_quote.save()

# def get_random_quote():
#     result = get_quotes(topic_list[random.randint(0, len(topic_list) - 1)])
#     return result

topic_list = get_topic()
print(topic_list)

# for topic in topic_list[92:]:
#     get_quotes(topic.lower())