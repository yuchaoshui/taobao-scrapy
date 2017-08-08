#!/usr/bin/env python2.7
# _*_ coding:utf-8 _*_

import argparse
import urllib, urllib2
import json
import time

def scrapy(k, pages):
    get_data_list = []
    for page in range(pages):
        print "getting page..."+str(page)
        time.sleep(2)
        postdata = {
                        'event_submit_do_new_search_auction': 1,
                        'search': '提交查询',
                        '_input_charset': 'utf-8',
                        'topSearch': 1,
                        'atype': 'b',
                        'searchfrom': 1,
                        'action': 'home:redirect_app_action',
                        'from': 1,
                        'q': k,
                        'sst': 1,
                        'n': 20,
                        'buying': 'buyitnow',
                        'm': 'api4h5',
                        'abtest': 16,
                        'wlsort': 16,
                        'style': 'list',
                        'closeModues': 'nav,selecthot,onesearch',
                        'page': page
                    }
        postdata = urllib.urlencode(postdata)
        url = "http://s.m.taobao.com/search?" + postdata

        ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        headers = {'Referer':'https://www.taobao.com/', 'User-Agent':ua}
        request = urllib2.Request(url, headers=headers)
        res = urllib2.urlopen(request, timeout=10)
        get_data = res.read()
        get_data_list.append(json.loads(get_data))

    return get_data_list


if __name__ == '__main__':

    data_dir = "./data/"
    parser = argparse.ArgumentParser(version='1.0')
    parser.add_argument('-k', '--keyword', action='append', required=True)
    parser.add_argument('-p', '--pages', default=10)
    args = parser.parse_args()
    p = int(args.pages)

    keywords = []
    for k in args.keyword:
        if k not in keywords:
            keywords.append(k)

    for k in keywords:
        with open(data_dir.rstrip("/")+"/"+k+".txt", 'w') as f:

            for one_page in scrapy(k,p):

                if one_page.get('result'):
                    for item in one_page.get("listItem"):
                        # 根据实际情况获取所需的字段，数据格式在 help.txt 文件中有示例。
                        title = item.get("title").encode("utf-8")
                        nick = item.get("nick").encode("utf-8")
                        f.write(nick+":\t"+title+"\n")
                        
                        
