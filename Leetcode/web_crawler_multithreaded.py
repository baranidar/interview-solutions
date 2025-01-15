#https://leetcode.com/problems/web-crawler-multithreaded/
#https://algo.monster/liteproblems/1242

# '''
# This is  HTMLParser's API interface
# You should not implement it or speculate the about its implementation

# class HTMLParser(object):
#     def getUrls(self, url):
#         '''
#         :type url: str
#         :rtype List[str]
#         '''
# '''

from collections import deque
from html.parser import HTMLParser
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed

class Solution:
    def crawl(startUrl: str, htmlParser: 'HTMLParser') -> List[str]:

        #get host name from Starturl
        host_name = lambda url: url.split('/')[2]
        #get our hostname so we can skip websites that is not in our domain
        our_site  = host_name(startUrl)
        #track pages we visited as we crawl.
        visited = set([startUrl])

        #initialize thread pool with max threads as needed. This is all going to run inside one process unlike multi-processing
        #following code will run under thread_ppol context
        with ThreadPoolExecutor(max_workers=5) as thread_pool:
            #submit to run in separate thread than parent thread and add the results to the queue
            queue = deque([thread_pool.submit(htmlParser.getUrls, our_site)])
            #if the queue is not empty and when the child thread completes
            while queue and as_completed:
                #popleft is better than pop(0) and has O(1) compared tot O(n)
                returned_urls = queue.popleft().result()
                for url in returned_urls:
                    #make sure we skip websites that is not in our domain
                    if host_name(url) == our_site and url not in visited:
                        # add to visited list
                        visited.add(url)
                        # add to queue again. This will run its own thread
                        queue.append(thread_pool.submit(htmlParser.getUrls, url))
        return list(visited)

# urls = [
#     "http://news.yahoo.com",
#     "http://news.yahoo.com/news",
#     "http://news.yahoo.com/news/topics",
#     "http://news.google.com"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = 'http://news.yahoo.com/news/topics'
# htmlParser = HTMLParser()
# result = crawl(startUrl, htmlParser)
# print(result)